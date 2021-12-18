import csp
import math
import sys
import time
import search
import utils
import pdb;
class PROBLEM(csp.CSP):

    def __init__(self, pvar,pdom,pctr):
        self.variables=[]
        self.domains=dict()
        self.neighbors=dict()
        self.size=0
        self.isindomain=dict()
        self.num_domains=0
        self.weight=dict()
        self.info=dict()
        self.dread(pdom)
        self.pread(pvar)
        self.cread(pctr)
        for i in range(0,self.size):
            self.variables.append(str(i))
        for Xi in self.variables:
            for Xj in self.neighbors[Xi]:
                self.weight[(Xi,Xj)]=1
                self.weight[(Xj,Xi)]=1

        csp.CSP.__init__(self,self.variables,self.domains,self.neighbors,self.constraints)



    def dread(self,pdom):
        lines=open(pdom,"r")
        
        l=lines.readlines()
        list=[]
        l[0]=l[0].strip("\n")
        num_domains=int(l[0])
        for i in range (1,len(l)):
            k=l[i].split()
            list.append(k)
        for line in list:
            domain_number=line[0]
            num_values=int(line[1])

            self.isindomain[domain_number]=[line[i] for i in range(2,num_values+2)]

    def pread(self,pvar):
        lines=open(pvar,"r")
        list=lines.readlines()
        list[0]=list[0].strip('\n')
        self.size=int(list[0])
        num_var=int(list[0])
        newlist=[]
        var=dict()
        logic=True
        for line in list:
            if logic==True:
                logic=False
                continue;
            Line=line.strip('\n')
            newlist.append(Line[-1:])

        for i in range(num_var):
            self.domains[str(i)]=self.isindomain[newlist[i]]



    def append_value(self,dict_obj, key, value):
        # Check if key exist in dict or not
        if key in dict_obj:
            # Key exist in dict.
            # Check if type of value of key is list or not
            if not isinstance(dict_obj[key],(list)):
                dict_obj[key] = list(dict_obj[key])
            dict_obj[key].append(value)
        else:
            # As key is not in dict,
            # so, add key-value pair
            dict_obj[key] = value

    def cread(self,pctr):
        f=open(pctr,"r")
        p=0
        lines=f.readlines()
        k=True
        for i in range (len(lines)):
            lines[i]=lines[i].strip('\n')
        list=[]
        for line in lines:
            l=line.split()
            list.append(l)
        for line in list:
            if k==True:
                k=False
                continue;
            successor=line[0]
            self.info[(line[0],line[1])]=[line[2],line[3]]
            self.info[(line[1],line[0])]=[line[2],line[3]]
            self.append_value(self.neighbors,line[0],line[1])
            self.append_value(self.neighbors,line[1],line[0])

    def getvar(self):
        return (self.variables)
    def getneig(self):
        return (self.neighbors)
    def getdomains(self):
        return (self.domains)

    def constraints(self,A,a,B,b):



        if (A,B) in self.info.keys():
            if self.info[(A,B)][0]==">":

                return (abs(int(a)-int(b))>int(self.info[(A,B)][1]))
            if self.info[(A,B)][0]=="=":


                return (abs(int(a)-int(b))==int(self.info[(A,B)][1]))






if __name__=='__main__':

    p=PROBLEM('var2-f24.txt',"dom2-f24.txt",'ctr2-f24.txt')
    begin=time.time()

    csp.backtracking_search(p,csp.mrv,inference=csp.forward_checking)
    end=time.time()
    print("the time is ",end-begin)
