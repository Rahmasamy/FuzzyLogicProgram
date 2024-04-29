from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk,Image
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plotLine
class fuzzy :
    def readfile(self):
        f = open("C:/Users/Owner/Downloads/fuzzyassigment/fuzzyfile.txt", 'r')
        content = f.read()
        content_list = content.split("\n")
        return content_list

    def __init__(self):
        self.content_list=self.readfile()
        self.variable1 = self.content_list[0]
        self.variable2 = self.content_list[1]
        self.variable3 = self.content_list[2] + self.content_list[3]
        self.variable4 = self.content_list[4]
        self.variable5 = self.content_list[5].split(" ")
        self.variable6 = self.content_list[6].split(" ")
        self.variable7 = self.content_list[7].split(" ")
        # 8,9,10
        self.variable8 = self.content_list[12].split(" ")  # ['beginner', 'TRI', '0', '15', '30']
        self.variable9 = self.content_list[13].split(" ")  # ['intermediate', 'TRI', '15', '30', '45']
        self.variable10 = self.content_list[14].split(" ")  # ['expert', 'TRI', '30', '60', '60']
        self.variable11 = self.content_list[15].split(" ")
        # 16,17,18
        self.variable19 = self.content_list[18].split(" ")  # ['very_low', 'TRAP', '0', '0', '10', '30']
        self.variable20 = self.content_list[19].split(" ")  # ['low', 'TRAP', '10', '30', '40', '60']
        self.variable21 = self.content_list[20].split(" ")  # ['medium', 'TRAP', '40', '60', '70', '90']
        self.variable22 = self.content_list[21].split(" ")  # ['high', 'TRAP', '70', '90', '100', '100']
        # 22,23,24
        self.variable26 = self.content_list[25].split(" ")
        self.variable27 = self.content_list[26].split(" ")
        self.variable28 = self.content_list[27].split(" ")

        # 28,29
        self.variable30 = self.content_list[30].split(
            " ")  # ['proj_funding', 'high', 'or', 'exp_level', 'expert', '=>', 'risk', 'low']
        self.variable31 = self.content_list[31].split(
            " ")  # ['proj_funding', 'medium', 'and', 'exp_level', 'intermediate', '=>', 'risk', 'normal']
        self.variable32 = self.content_list[32].split(" ")
        self.variable33 = self.content_list[33].split(" ")
        self.variable34 = self.content_list[34].split(" ")
        self.input=""
        self.name=[]
        self.type=[]
        self.lower=[]
        self.upper=0
        self.flag1=0
        self.flag2=0
        self.flag3=0
        self.fuzzysetname=[]
        self.fuzzyset_type=[]
        self.values=[]
        self.rule_1=[]
        self.rule_2=[]
        self.rule_3=[]
        self.rule_4=[]
        self.rule_5=[]
        self.f=0
        self.f2=0
        self.f3=0


    def add_variable(self):
     self.flag1=1
     print("----------------------add variables in progress---------------------------------")
     for i in range (0,3):

         if i==0:
          self.name.append(self.variable5[0])
          self.type.append(self.variable5[1])
          self.lower.append(self.variable5[2])
         elif i==1:
            self.name.append(self.variable6[0])
            self.type.append(self.variable6[1])
            self.lower.append(self.variable6[2])
         else :
            self.name.append(self.variable7[0])
            self.type.append(self.variable7[1])
            self.lower.append(self.variable7[2])

     for i in range(0,3):
      print(f"the name of {i+1}st is ",self.name[i],f"the type of {i+1}st is ",self.type[i],"the range is",self.lower[i])
     print("--------------------the fuuzy varible have been added-------------------- ")

    def fuzzy_exp(self):
        # print(self.content_list[11]) exp_level
        if self.name[0] == self.content_list[11]:

            for i in range(0, 3):
                if i == 0:
                    self.fuzzysetname.append(self.variable8[0])
                    self.fuzzyset_type.append(self.variable8[1])
                    self.values.append(self.variable8[2:])
                elif i == 1:
                    self.fuzzysetname.append(self.variable9[0])
                    self.fuzzyset_type.append(self.variable9[1])
                    self.values.append(self.variable9[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable10[0])
                    self.fuzzyset_type.append(self.variable10[1])
                    self.values.append(self.variable10[2:])

        elif self.name[1] == self.content_list[11]:
            for i in range(0, 3):

                if i == 0:
                    self.fuzzysetname.append(self.variable8[0])
                    self.fuzzyset_type.append(self.variable8[1])
                    self.values.append(self.variable8[2:])

                elif i == 1:
                    self.fuzzysetname.append(self.variable9[0])
                    self.fuzzyset_type.append(self.variable9[1])
                    self.values.append(self.variable9[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable10[0])
                    self.fuzzyset_type.append(self.variable10[1])
                    self.values.append(self.variable10[2:])

        elif self.name[2] == self.content_list[11]:
            for i in range(0, 3):

                if i == 0:
                    self.fuzzysetname.append(self.variable8[0])
                    self.fuzzyset_type.append(self.variable8[1])
                    self.values.append(self.variable8[2:])
                    print("?????", self.fuzzysetname)
                elif i == 1:
                    self.fuzzysetname.append(self.variable9[0])
                    self.fuzzyset_type.append(self.variable9[1])
                    self.values.append(self.variable9[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable10[0])
                    self.fuzzyset_type.append(self.variable10[1])
                    self.values.append(self.variable10[2:])
        return self.fuzzysetname,self.fuzzyset_type,self.values
    def fuzzy_proj(self):
        # print("{{{",self.content_list[17])
        if self.name[0] == self.content_list[17]:
            for i in range(0, 4):
                if i == 0:
                    self.fuzzysetname.append(self.variable19[0])
                    self.fuzzyset_type.append(self.variable19[1])
                    self.values.append(self.variable19[2:])
                elif i == 1:
                    self.fuzzysetname.append(self.variable20[0])
                    self.fuzzyset_type.append(self.variable20[1])
                    self.values.append(self.variable20[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable21[0])
                    self.fuzzyset_type.append(self.variable21[1])
                    self.values.append(self.variable21[2:])
                elif i == 3:
                    self.fuzzysetname.append(self.variable22[0])
                    self.fuzzyset_type.append(self.variable22[1])
                    self.values.append(self.variable22[2:])

        elif self.name[1] == self.content_list[17]:
            for i in range(0, 4):
                if i == 0:
                    self.fuzzysetname.append(self.variable19[0])
                    self.fuzzyset_type.append(self.variable19[1])
                    self.values.append(self.variable19[2:])

                elif i == 1:
                    self.fuzzysetname.append(self.variable20[0])
                    self.fuzzyset_type.append(self.variable20[1])
                    self.values.append(self.variable20[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable21[0])
                    self.fuzzyset_type.append(self.variable21[1])
                    self.values.append(self.variable21[2:])
                elif i == 3:
                    self.fuzzysetname.append(self.variable22[0])
                    self.fuzzyset_type.append(self.variable22[1])
                    self.values.append(self.variable22[2:])
        elif self.name[2] == self.content_list[17]:
            for i in range(0, 4):
                if i == 0:
                    self.fuzzysetname.append(self.variable19[0])
                    self.fuzzyset_type.append(self.variable19[1])
                    self.values.append(self.variable19[2:])

                elif i == 1:
                    self.fuzzysetname.append(self.variable20[0])
                    self.fuzzyset_type.append(self.variable20[1])
                    self.values.append(self.variable20[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable21[0])
                    self.fuzzyset_type.append(self.variable21[1])
                    self.values.append(self.variable21[2:])
                elif i == 3:
                    self.fuzzysetname.append(self.variable22[0])
                    self.fuzzyset_type.append(self.variable22[1])
                    self.values.append(self.variable22[2:])
        return self.fuzzysetname,self.fuzzyset_type,self.values
    def fuzzy_risk(self):
        if self.name[0]==self.content_list[24]:
           for i in range(0,3):
               if i==0:
                self.fuzzysetname.append(self.variable26[0])
                self.fuzzyset_type.append(self.variable26[1])
                self.values.append(self.variable26[2:])
               elif i==1 :
                   self.fuzzysetname.append(self.variable27[0])
                   self.fuzzyset_type.append(self.variable27[1])
                   self.values.append(self.variable27[2:])
               elif i==2 :
                   self.fuzzysetname.append(self.variable28[0])
                   self.fuzzyset_type.append(self.variable28[1])
                   self.values.append(self.variable28[2:])

        elif self.name[1]==self.content_list[24]:
            for i in range(0, 3):
                if i == 0:
                    self.fuzzysetname.append(self.variable26[0])
                    self.fuzzyset_type.append(self.variable26[1])
                    self.values.append(self.variable26[2:])

                elif i == 1:
                    self.fuzzysetname.append(self.variable27[0])
                    self.fuzzyset_type.append(self.variable27[1])
                    self.values.append(self.variable27[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable28[0])
                    self.fuzzyset_type.append(self.variable28[1])
                    self.values.append(self.variable28[2:])
        elif self.name[2]==self.content_list[24]:
            for i in range(0, 3):
                if i == 0:
                    self.fuzzysetname.append(self.variable26[0])
                    self.fuzzyset_type.append(self.variable26[1])
                    self.values.append(self.variable26[2:])
                elif i == 1:
                    self.fuzzysetname.append(self.variable27[0])
                    self.fuzzyset_type.append(self.variable27[1])
                    self.values.append(self.variable27[2:])
                elif i == 2:
                    self.fuzzysetname.append(self.variable28[0])
                    self.fuzzyset_type.append(self.variable28[1])
                    self.values.append(self.variable28[2:])
        #print("the fuzzy sets names,type ,values are ")
        return self.fuzzysetname,self.fuzzyset_type,self.values
    def add_fuzzy_sets(self):
        self.flag2=1
        print("Enter the variable’s name:")
        print("--------------------------")
        print("adding fuzzy set from file is start...")
        # if
        if self.f==0 and self.f2==0 and self.content_list[11]=="exp_level":
         self.fuzzysetname,self.fuzzyset_type,self.values= self.fuzzy_exp()
         self.f=1

        elif self.f2==0 and self.f==1 and self.content_list[17]=="proj_funding":
         self.fuzzysetname,self.fuzzyset_type,self.values=self.fuzzy_proj()
         self.f2 = 1

        elif self.f2==1 and self.content_list[24]=="risk":
         self.fuzzysetname,self.fuzzyset_type,self.values=self.fuzzy_risk()

        #print("ggggggg",self.content_list[23]) risk
        #print("{{{]]]]]",self.content_list[24])

        for i in range(0,len(self.fuzzysetname)):
            print("the fuzzy set 's name 's", self.fuzzysetname[i], "and the type is ", self.fuzzyset_type[i],
                      " and the values is", self.values[i])
        print("===================================================================")

    def fuzzifcation_TRA(self):

        beg = []
        inter = []
        exp = []
        b1 = [0]
        b2 = [1]
        b3 = [0]
        ###########################
        i1 = [0]
        i2 = [1]
        i3 = [0]
        ######################
        e1 = [0]
        e2 = [1]
        e3 = [0]
        for i in range(2, 5):
            beg.append(int(self.variable8[i]))
            inter.append(int(self.variable9[i]))
            exp.append(int(self.variable10[i]))
            if i == 2:
                b1.append(int(self.variable8[i]))
                b1.reverse()
                i1.append(int(self.variable9[i]))
                i1.reverse()
                e1.append(int(self.variable10[i]))
                e1.reverse()

            if i == 3:
                b2.append(int(self.variable8[i]))
                b2.reverse()
                i2.append(int(self.variable9[i]))
                i2.reverse()
                e2.append(int(self.variable10[i]))
                e2.reverse()
            if i == 4:
                b3.append(int(self.variable8[i]))
                b3.reverse()
                i3.append(int(self.variable9[i]))
                i3.reverse()
                e3.append(int(self.variable10[i]))
                e3.reverse()

        c = {
            "beg": {"point1": b1, "point2": b2, "point3": b3}
            , "inter": {"point1": i1, "point2": i2, "point3": i3},
            "exp": {"point1": e1, "point2": e2, "point3": e3}
        }
        # print(c["beg"]["point1"][0], c["beg"]["point2"][0], c["beg"]["point3"][0])
        # print(c["inter"]["point1"][0], c["inter"]["point2"][0], c["inter"]["point3"][0])
        # print(c["exp"]["point1"][0], c["exp"]["point2"][0], c["exp"]["point3"][0])
        # inter =====> 45
        # exp ===> 30
        input = int(self.content_list[38])
        # print(input)

        if input <= c["beg"]["point1"][0] + 10 and input >= c["beg"]["point2"][0] - 10:
            xy = c["beg"]["point1"]
            x2y2 = c["beg"]["point2"]
        elif input <= c["beg"]["point2"][0] + 10 and input >= c["beg"]["point3"][0] - 10:

            xy = c["beg"]["point2"]
            x2y2 = c["beg"]["point3"]
        elif input <= c["inter"]["point1"][0] + 10 and input >= c["inter"]["point2"][0] - 10:
            xy = c["inter"]["point1"]
            x2y2 = c["inter"]["point2"]
        elif input <= c["inter"]["point2"][0] + 10 and input >= c["inter"]["point3"][0] - 10:
            xy = c["inter"]["point2"]
            x2y2 = c["inter"]["point3"]
            # print("the first poins are", xy)
            # print("the second points are", x2y2)
        if input <= c["exp"]["point1"][0] + 10 or input >= c["exp"]["point2"][0] - 10:

            x1y1 = c["exp"]["point1"]
            x22y22 = c["exp"]["point2"]
            # print(x1y1, x22y22)
        elif input <= c["exp"]["point2"][0] + 10 and input >= c["exp"]["point3"][0] - 10:
            xy = c["exp"]["point2"]
            x2y2 = c["exp"]["point3"]
        # get slope for intermediate
        # xy====> # [30,1]
        # x2y2=====> [45,0]
        slope = (x2y2[1] - xy[1]) / (x2y2[0] - xy[0])
        #print("the slope is ", slope)
        # get slope for expert
        slope2 = (x22y22[1] - x1y1[1]) / (x22y22[0] - x1y1[0])
        # get any point from line and substitiute
        # print(xy)  # [30,1] #  ===> intermidate
        # print(x2y2)  # [45,0]
        # print(x1y1)  # [30, 0]
        # print(x22y22)  # [60, 1]
        bias_inter = xy[1] - slope * xy[0]
        #print("the bias is ", bias_inter)  # 3
        bias_exp = x1y1[1] - slope2 * x1y1[0]
        #print("the bias is ", bias_exp)  # -1
        # y=ax+b ,x===>40
        y_inter = input * slope + bias_inter
        #print("the y for inter mediate is", y_inter)
        y_exp = input * slope2 + bias_exp
        #print("the y for expert is", y_exp)
        return slope,slope2,bias_inter,bias_exp,y_inter, y_exp
    def add_rules(self):
        self.flag3=1
        self.rule_1.append(self.variable30)
        self.rule_2.append(self.variable31)
        self.rule_3.append(self.variable32)
        self.rule_4.append(self.variable33)
        self.rule_5.append(self.variable34)
        print("the rules is ")
        print("rule 1 ===>",self.rule_1)
        print("rule 2 ===>", self.rule_2)
        print("rule 3 ===>", self.rule_3)
        print("rule 4 ===>", self.rule_4)
        print("rule 5 ===>", self.rule_5)

    def fuzifcation_TRAP(self):
        very_low = []
        low = []
        meduim = []
        high = []
        v_l1 = [0]
        v_l2 = [1]
        v_l3 = [1]
        v_l4 = [0]
        ###########################
        l_1 = [0]
        l_2 = [1]
        l_3 = [1]
        l_4 = [0]
        ######################
        m_1 = [0]
        m_2 = [1]
        m_3 = [1]
        m_4 = [0]
        #####################
        h_1 = [0]
        h_2 = [1]
        h_3 = [1]
        h_4 = [0]
        for i in range(2, 6):
            very_low.append(int(self.variable19[i]))
            low.append(int(self.variable20[i]))
            meduim.append(int(self.variable21[i]))
            high.append(int(self.variable22[i]))
            if i == 2:
                v_l1.append(int(self.variable19[i]))
                v_l1.reverse()
                l_1.append(int(self.variable20[i]))
                l_1.reverse()
                m_1.append(int(self.variable21[i]))
                m_1.reverse()
                h_1.append(int(self.variable22[i]))
                h_1.reverse()
            if i == 3:
                v_l2.append(int(self.variable19[i]))
                v_l2.reverse()
                l_2.append(int(self.variable20[i]))
                l_2.reverse()
                m_2.append(int(self.variable21[i]))
                m_2.reverse()
                h_2.append(int(self.variable22[i]))
                h_2.reverse()
            if i == 4:
                v_l3.append(int(self.variable19[i]))
                v_l3.reverse()
                l_3.append(int(self.variable20[i]))
                l_3.reverse()
                m_3.append(int(self.variable21[i]))
                m_3.reverse()
                h_3.append(int(self.variable22[i]))
                h_3.reverse()
            if i == 5:
                v_l4.append(int(self.variable19[i]))
                v_l4.reverse()
                l_4.append(int(self.variable20[i]))
                l_4.reverse()
                m_4.append(int(self.variable21[i]))
                m_4.reverse()
                h_4.append(int(self.variable22[i]))
                h_4.reverse()

        temp = {
            "very_low": {"point1": v_l1, "point2": v_l2, "point3": v_l3, "point4": v_l4}
            , "low": {"point1": l_1, "point2": l_2, "point3": l_3, "point4": l_4},
            "meduim": {"point1": m_1, "point2": m_2, "point3": m_3, "point4": m_4},
            "high": {"point1": h_1, "point2": h_2, "point3": h_3, "point4": h_4}}

        # get x axsis for all points in the dictionary
        # print(temp["very_low"]["point1"][0], temp["very_low"]["point2"][0], temp["very_low"]["point3"][0], temp["very_low"]["point4"][0])
        # print(temp["low"]["point1"][0], temp["low"]["point2"][0], temp["low"]["point3"][0], temp["low"]["point4"][0])
        # print(temp["meduim"]["point1"][0], temp["meduim"]["point2"][0], temp["meduim"]["point3"][0],temp["meduim"]["point4"][0])
        # print(temp["high"]["point1"][0], temp["high"]["point2"][0], temp["high"]["point3"][0], temp["high"]["point4"][0])

        input2 = int(self.content_list[37])  # 50

        if input2 <= temp["very_low"]["point1"][0] + 10 and input2 >= temp["very_low"]["point2"][0] - 10:
            xtyt = temp["very_low"]["point1"]
            xt2yt2 = temp["very_low"]["point2"]
        elif input2 <= temp["very_low"]["point2"][0] + 10 and input2 >= temp["very_low"]["point3"][0] - 10:

            xtyt = temp["very_low"]["point2"]
            xt2yt2 = temp["very_low"]["point3"]
        elif input2 <= temp["very_low"]["point3"][0] + 10 and input2 >= temp["very_low"]["point4"][0] - 10:
            xtyt = temp["very_low"]["point3"]
            xt2yt2 = temp["very_low"]["point4"]

        elif input2 <= temp["low"]["point1"][0] + 10 and input2 >= temp["low"]["point2"][0] - 10:
            xtyt = temp["low"]["point1"]
            xt2yt2 = temp["low"]["point2"]
        elif input2 <= temp["low"]["point2"][0] + 10 and input2 >= temp["low"]["point3"][0] - 10:
            xtyt = temp["low"]["point2"]
            xt2yt2 = temp["low"]["point3"]
        # ===================================>
        elif input2 <= temp["low"]["point3"][0] + 10 and input2 >= temp["low"]["point4"][0] - 10:
            xtyt = temp["low"]["point3"]
            xt2yt2 = temp["low"]["point4"]
            ######### low

        # ===================================>
        if input2 <= temp["meduim"]["point1"][0] + 10 and input2 >= temp["meduim"]["point2"][0] - 10:
            ############ meduim
            xt3yt3 = temp["meduim"]["point1"]
            xt23yt23 = temp["meduim"]["point2"]
        elif input2 <= temp["meduim"]["point2"][0] + 10 and input2 >= temp["meduim"]["point3"][0] - 10:
            xtyt = temp["meduim"]["point2"]
            xt2yt2 = temp["meduim"]["point3"]
        elif input2 <= temp["meduim"]["point3"][0] + 10 and input2 >= temp["meduim"]["point4"][0] - 10:
            xtyt = temp["meduim"]["point3"]
            xt2yt2 = temp["meduim"]["point4"]
        elif input2 <= temp["high"]["point1"][0] + 10 and input2 >= temp["high"]["point2"][0] - 10:
            xtyt = temp["high"]["point1"]
            xt2yt2 = temp["high"]["point2"]
        elif input2 <= temp["high"]["point2"][0] + 10 and input2 >= temp["high"]["point3"][0] - 10:
            xtyt = temp["high"]["point2"]
            xt2yt2 = temp["high"]["point3"]
        elif input2 <= temp["high"]["point3"][0] + 10 and input2 >= temp["high"]["point4"][0] - 10:
            xtyt = temp["high"]["point3"]
            xt2yt2 = temp["high"]["point4"]
        # slope for low
        slope_trap = (xt2yt2[1] - xtyt[1]) / (xt2yt2[0] - xtyt[0])
        #print("the slope for trap for low is ", slope_trap)
        # get slope for meduim
        slope_trap2 = (xt23yt23[1] - xt3yt3[1]) / (xt23yt23[0] - xt3yt3[0])
        #print("the slope for trap for meduim  is ", slope_trap2)
        bias_low = xtyt[1] - slope_trap * xtyt[0]
        #print("the bias is ", bias_low)  # 3
        bias_meduim = xt3yt3[1] - slope_trap2 * xt3yt3[0]
        #print("the bias is ", bias_meduim)  # -1
        # y=ax+b ,x===>40
        y_low = input2 * slope_trap + bias_low
        #print("the y for low is", y_low)
        y_med = input2 * slope_trap2 + bias_meduim
        #print("the y for meduim is", y_med)
        return slope_trap,slope_trap2,bias_low,bias_meduim,y_low, y_med

    def apply_rules(self,rule_5):
        slope,slope2,bias_inter,bias_exp,y_inter, y_exp= self.fuzzifcation_TRA()
        slope_trap, slope_trap2, bias_low, bias_meduim, y_low, y_med= self.fuzifcation_TRAP()
        q = y_low + 1
        q2 = y_low + 2
        dic = {
            "exp_level": {y_inter: "intermediate", y_exp: "expert"},
            "proj_funding": {q: "low", q2: "medium"}
        }
        l = []
        l.extend(dic.keys())
        x2 = rule_5[0][0]  # proj-funding
        y22 = rule_5[0][3]  # exp
        #############################
        keyss = []
        keyss2 = []
        keyss3 = []
        keyss2.extend(dic["proj_funding"].keys())
        keyss.extend(dic["exp_level"].keys())
        keyss3.append(keyss2[0] - 1)
        keyss3.append(keyss2[1] - 2)
        if dic[x2][q] == rule_5[0][1] or dic[x2][q2] == rule_5[0][1]:
            if rule_5[0][2] == "or":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:

                    m4 = max(keyss[0], keyss3[0])
                else:
                    m4 = max(0, keyss3[0])
            if rule_5[0][2] == "and":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:

                    m4 = min(keyss[0], keyss3[0])
                else:
                    m4 = min(0, keyss3[0])
            if rule_5[0][2] == "and_not":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:

                    m4 = min(1 - keyss[0], keyss3[0])
                else:
                    m4 = min(0, keyss3[0])
        else:
            if rule_5[0][2] == "or":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:

                    m4 = max(0, keyss[0])
                else:
                    m4 = max(0, 0)

            elif rule_5[0][2] == "and":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:
                    m4 = min(0, keyss[0])
                else:
                    m4 = min(0, 0)
            elif rule_5[0][2] == "and_not":
                if dic[y22][y_inter] == rule_5[0][4] or dic[y22][y_exp] == rule_5[0][4]:
                    m4 = min(0, 1 - keyss[0])
                else:
                    m4 = min(0, 0)
        return m4
    def inference(self):
        inf1=self.apply_rules(self.rule_1)
        inf2 = self.apply_rules(self.rule_2)
        inf3=self.apply_rules(self.rule_3)
        inf4=self.apply_rules(self.rule_4)
        inf5=self.apply_rules(self.rule_5)
        return inf1,inf2,inf3,inf4,inf5

    def plotting_slop(self):
        slope_trap, slope_trap2, bias_meduim, bias_low, y_low, y_med = self.fuzifcation_TRAP()
        # print(slope_trap,slope_trap2)
        sp = np.arange(slope_trap, 0, 0.01)
        # print(sp)
        sp2 = np.arange(0, slope_trap2, 0.01)
        # print(sp2)
        ypred = np.arange(0, 1, 0.2)
        # print(ypred)
        plt.plot(sp, ypred, 'b', linewidth=1.5, label="SLOPE1-TRAP")
        plt.plot(sp2, ypred, 'r', linewidth=1.5, label="SLOPE2-TRAP")
        plt.title("variable-slope ")
        plt.legend()
        plt.show()

    def plotting_slop_constant_TRAP(self):
        slope_trap, slope_trap2, bias_meduim, bias_low, y_low, y_med = self.fuzifcation_TRAP()
        y = [2, 1, 0, -1, -2, -3]
        x = [slope_trap, slope_trap, slope_trap, slope_trap, slope_trap, slope_trap]
        x2 = [slope_trap2, slope_trap2, slope_trap2, slope_trap2, slope_trap2, slope_trap2]
        plotLine.plot(x, y, 'b', label="slop1")
        plotLine.plot(x2, y, 'g', label="slop2")
        plotLine.title("slop-constant for TRAP")
        plotLine.legend()
        plotLine.show()

    def plotting_bias_constant_trap(self):
        slope_trap, slope_trap2, bias_meduim, bias_low, y_low, y_med = self.fuzifcation_TRAP()
        y = [2, 1, 0, -1, -2, -3]
        x = [bias_meduim, bias_meduim, bias_meduim, bias_meduim, bias_meduim, bias_meduim]
        x2 = [bias_low, bias_low, bias_low, bias_low, bias_low, bias_low]
        plotLine.plot(x, y, 'c', label="bias-TRAP1")
        plotLine.plot(x2, y, 'orange', label="bias-TRAP2")
        plotLine.title("bias-constant for TRAP")
        plotLine.legend()
        plotLine.show()

    def plotting_bias_constant_TRA(self):
        slope_trap, slope_trap2, bias_meduim, bias_low, y_low, y_med = self.fuzzifcation_TRA()
        y = [2, 1, 0, -1, -2, -3]
        x = [bias_meduim, bias_meduim, bias_meduim, bias_meduim, bias_meduim, bias_meduim]
        x2 = [bias_low, bias_low, bias_low, bias_low, bias_low, bias_low]
        plotLine.plot(x, y, 'brown', label="bias-TRA1")
        plotLine.plot(x2, y, 'pink', label="bias-TRA2")
        plotLine.title("bias-constant for TRA")
        plotLine.legend()
        plotLine.show()

    def plotting_slope_constant_TRA(self):
        slope, slope2, bias_meduim, bias_low, y_low, y_med = self.fuzzifcation_TRA()
        y = [2, 1, 0, -1, -2, -3]
        x = [slope, slope, slope, slope, slope, slope]
        x2 = [slope2, slope2, slope2, slope2, slope2, slope2]
        plotLine.plot(x, y, 'blue', label="slop-TRA1")
        plotLine.plot(x2, y, 'maroon', label="slop-TRA2")
        plotLine.title("slope-constant TRA ")
        plotLine.legend()
        plotLine.show()

    def plotting_bias_TRAP(self):
        slope_trap, slope_trap2, bias_meduim, bias_low, y_low, y_med = self.fuzifcation_TRAP()
        #print(bias_meduim,bias_low)
        biasm = np.arange(bias_meduim, 0, -0.05)
        #print(biasm)
        biasm_new = biasm[:20]
        biasl = np.arange(bias_low ,0, 0.1)
        # print(biasl.shape)
        ypred = np.arange(0, 1, 0.03)
        y_predn = ypred[:20]
        print(biasm_new.shape)
        print(y_predn.shape)
        print(biasl.shape)
        plt.plot(biasm_new, y_predn, 'b', linewidth=1.5, label="bias1-TRAP")
        plt.plot(biasl, y_predn, 'r', linewidth=1.5, label="bias2-TRAP")
        plt.legend()
        plt.show()

    def plot_inference(self):
        # plot constant inference
        inf1, inf2, inf3, inf4, inf5 = self.inference()
        y = [2, 1, 0, -1, -2, -3]
        x = [inf1, inf1, inf1, inf1, inf1, inf1]
        x2 = [inf2 + 0.005, inf2 + 0.005, inf2 + 0.005, inf2 + 0.005, inf2 + 0.005, inf2 + 0.005]
        x3 = [inf3 + 0.01, inf3 + 0.01, inf3 + 0.01, inf3 + 0.01, inf3 + 0.01, inf3 + 0.01]
        x4 = [inf4 + 0.005, inf4 + 0.005, inf4 + 0.005, inf4 + 0.005, inf4 + 0.005, inf4 + 0.005]
        x5 = [inf5 + 0.02, inf5 + 0.02, inf5 + 0.02, inf5 + 0.02, inf5 + 0.02, inf5 + 0.02]
        plotLine.plot(x, y, 'b', label="inference1")
        plotLine.plot(x2, y, 'g', label="inference2")
        plotLine.plot(x3, y, 'r', label="inference3")
        plotLine.plot(x4, y, 'y', label="inference4")
        plotLine.plot(x5, y, 'c', label="inference5")
        plotLine.title(" inference after apply Rules")
        plotLine.legend()
        plotLine.show()
    def defuzzification(self):
        i1,i2,i3,i4,i5=self.inference()
        i44=i4+1
        i55=i5+2
        dic2 = {
            "rule1": {i1: self.rule_1[0][7]},
            "rule2": {i2: self.rule_2[0][7]},
            "rule3": {i3: self.rule_3[0][7]},
            "rule4": {i44: self.rule_4[0][7]},
            "rule5": {i55: self.rule_5[0][7]}
        }
        l1=[]
        l2=[]
        l3=[]
        l1.append(int(self.values[-3:][0][0]))
        l1.append(int(self.values[-3:][0][1]))
        l1.append(int(self.values[-3:][0][2]))
        l2.append(int(self.values[-3:][1][0]))
        l2.append(int(self.values[-3:][1][1]))
        l2.append(int(self.values[-3:][1][2]))
        l3.append(int(self.values[-3:][2][0]))
        l3.append(int(self.values[-3:][2][1]))
        l3.append(int(self.values[-3:][2][2]))
        #l2.append(int(self.values[-3:][1]))
        #l3.append(int(self.values[-3:][2]))
        #print(l1,l2,l3)
        # 0.3333333333333335 0.3333333333333335 0 0 0
        centrod1 = (l1[2] + l1[0]) / 2
        centroid2 = (l2[2] + l2[0]) / 2
        centroid3 = (l3[2] + l3[0]) / 2
        # dictionary for centroids
        dic3 = {
            "low": centrod1, "normal": centroid2, "high": centroid3
        }
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        if dic2["rule1"][i1] == "low" and i1 != 0:
            c1 = dic3["low"]
        elif dic2["rule1"][i1] == "normal" and i1 != 0:
            c1 = dic3["normal"]
        elif dic2["rule1"][i1] == "high" and i1 != 0:
            c1 = dic3["high"]
        if dic2["rule2"][i2] == "low" and i2 != 0:
            c2 = dic3["low"]
        elif dic2["rule2"][i2] == "normal" and i2 != 0:
            c2 = dic3["normal"]
        elif dic2["rule2"][i2] == "high" and i2 != 0:
            c2 = dic3["high"]
        if dic2["rule3"][i3] == "low" and i3 != 0:
            c3 = dic3["low"]
        elif dic2["rule3"][i3] == "normal" and i3 != 0:
            c3 = dic3["normal"]
        elif dic2["rule3"][i3] == "high" and i3 != 0:
            c3 = dic3["high"]
        if dic2["rule4"][i44] == "low" and i44 - 1 != 0:
            c4 = dic3["low"]
        elif dic2["rule4"][i44] == "normal" and i44 - 1 != 0:
            c4 = dic3["normal"]
        elif dic2["rule4"][i44] == "high" and i44 - 1 != 0:
            c4 = dic3["high"]
        if dic2["rule5"][i55] == "low" and i55 - 2 != 0:
            c5 = dic3["low"]
        elif dic2["rule5"][i55] == "normal" and i55 - 2 != 0:
            c5 = dic3["normal"]
        elif dic2["rule5"][i55] == "high" and i55 - 2 != 0:
            c5 = dic3["high"]
        ii = i44 - 1
        ii2 = i55 - 2
        weighted_mean = (c1 * i1 + c2 * i2 + c3 * i3 + c4 * ii + c5 * ii2) / (i1 + i2 + i3 + ii + ii2)


        return weighted_mean

    def risk(self):
        risk = np.arange(0, 101, 1)
        risk_1 = fuzz.trimf(risk, [0, 25, 50])
        risk_2 = fuzz.trimf(risk, [25, 50, 75])
        risk_3 = fuzz.trimf(risk, [50, 100, 100])
        plt.plot(risk, risk_1, 'b', linewidth=1.5, label='low')
        plt.plot(risk, risk_2, 'g', linewidth=1.5, label='normal')
        plt.plot(risk, risk_3, 'r', linewidth=1.5, label='high')
        plt.xlabel("range(0,100)")
        plt.ylabel("predict between 0,1")
        plt.title('Risk')
        plt.show()

    def exp_level(self):
        exp_level = np.arange(0, 61, 1)
        exp_level_1 = fuzz.trimf(exp_level, [0, 15, 30])
        exp_level_2 = fuzz.trimf(exp_level, [15, 30, 45])
        exp_level_3 = fuzz.trimf(exp_level, [30, 60, 60])
        plt.plot(exp_level, exp_level_1, 'b', linewidth=1.5, label='low')
        plt.plot(exp_level, exp_level_2, 'g', linewidth=1.5, label='normal')
        plt.plot(exp_level, exp_level_3, 'r', linewidth=1.5, label='high')
        plt.xlabel("range(0,60)")
        plt.ylabel("predict between 0,1")
        plt.title('EXP-LEVEL')
        plt.show()

    def proi_funding(self):
        proj_funding = np.arange(0, 101, 1)
        proj_funding_1 = fuzz.trapmf(proj_funding, [0, 0, 10, 30])
        proj_funding_2 = fuzz.trapmf(proj_funding, [10, 30, 40, 60])
        proj_funding_3 = fuzz.trapmf(proj_funding, [40, 60, 70, 90])
        proj_funding_4 = fuzz.trapmf(proj_funding, [70, 90, 100, 100])
        plt.plot(proj_funding, proj_funding_1, 'b', linewidth=1.5, label='very_low')
        plt.plot(proj_funding, proj_funding_2, 'g', linewidth=1.5, label='low')
        plt.plot(proj_funding, proj_funding_3, 'r', linewidth=1.5, label='medium')
        plt.plot(proj_funding, proj_funding_4, 'r', linewidth=1.5, label='high ')
        plt.xlabel("range(0,100)")
        plt.ylabel("predict between 0,1")
        plt.title('proj-funding')
        plt.show()
    def run_simulation(self):
        if self.flag1==0 or self.flag2==0 or self.flag3==0:
            print("CAN’T START THE SIMULATION! Please add the fuzzy sets and rules first.")
            return
        print("Enter the crisp values")
        print("----------------------------")
        print("the predicted  is normal ",self.defuzzification())

    def plot_prediction(self):
        risk = np.arange(0, 101, 1)
        risk_1 = fuzz.trimf(risk, [0, 25, 50])
        risk_2 = fuzz.trimf(risk, [25, 50, 75])
        risk_3 = fuzz.trimf(risk, [50, 100, 100])
        wegihted_mean=self.defuzzification()

        plt.plot(risk, risk_1, 'b', linewidth=1.5, label='low')
        plt.plot(risk, risk_2, 'g', linewidth=1.5, label='normal')
        plt.plot(risk, risk_3, 'r', linewidth=1.5, label='high')
        x=[wegihted_mean,wegihted_mean,wegihted_mean,wegihted_mean,wegihted_mean,wegihted_mean]
        y=[0,0.2,0.4,0.6,0.8,1]
        plotLine.plot(x, y, 'tab:pink', label="predction")
        plt.xlabel("range(0,100)")
        plt.ylabel("predict between 0,1")
        plt.title('Risk')
        plt.legend()
        plotLine.legend()
        plt.show()
        plotLine.show()

    def plotting_variable_slop_TRA(self):
        slope, slope2, bias_inter, bias_exp, y_inter, y_exp = self.fuzzifcation_TRA()
        x1slop1 = np.arange(slope, 0, 0.01)
        x1slop2 = np.arange(0, slope2, 0.01)
        x1 = x1slop1[:4]
        y_pred = np.arange(0, 0.8, 0.2)
        plt.plot(x1, y_pred, 'g', linewidth=1.5, label='slope1-TRA')
        plt.plot(x1slop2, y_pred, 'b', linewidth=1.5, label='slope2-TRA')
        plt.title("variable slope TRA")
        plt.legend()
        plt.show()

    def plotting_variable_bias_TRA(self):
        slope, slope2, bias_inter, bias_exp, y_inter, y_exp = self.fuzzifcation_TRA()
        #print(bias_inter)
        #print(bias_exp)
        bias_x_1 = np.arange(0, bias_inter, 0.2)
        bias_x_2 = np.arange(bias_exp, 0, 0.1)
        bias_x_1 = bias_x_1[:10]
        y_pred = np.arange(0, 1, 0.1)
        # print(y_pred.shape)
        plt.plot(bias_x_1, y_pred, 'b', linewidth=1.5, label='bias1-TRA')
        plt.plot(bias_x_2, y_pred, 'g', linewidth=1.5, label='bias2--TRA')
        plt.title("variable bias TRA")
        plt.legend()
        plt.show()
    def menue(self):
        print("Main Menu")
        print("== == == == ==")
        print("1 - Add variables.")
        print("2 - Add fuzzy sets to an existing variable.")
        print("3 - Add rules.")
        print("4 - Run the simulation on crisp values.")

    def main_menue(self):
        print("Enter the system’s name and a brief description:")
        print("------------------------------------------------")
        print(self.variable2)
        print(self.variable3)
        print("\n")
        self.menue()
        if self.variable4 =="1":
             self.add_variable()
             del self.variable4

        elif self.variable4 =="2":
             self.add_fuzzy_sets()
             del self.variable4
        elif self.variable4=="3":
             self.add_rules()
             del self.variable4
        elif self.variable4=="4":
             self.run_simulation()
             del self.variable4

        if self.content_list[8] =='x':
             self.menue()
             #del self.content_list[8]
        elif self.content_list[8] =="1":
             self.add_variable()
             #del self.content_list[8]
        elif self.content_list[8] =="2":
             self.add_fuzzy_sets()
             #del self.content_list[8]
        elif self.content_list[8]=="3":
             self.add_rules()
             #del self.content_list[8]
        elif self.content_list[8]=="4":
             self.run_simulation()
             #del self.content_list[8]
        #print(self.content_list[9]) # 4
        if self.content_list[9] =="1":
             self.add_variable()
             #del self.content_list[9]
        elif self.content_list[9] =="2":
             self.add_fuzzy_sets()
             #del self.content_list[9]
        elif self.content_list[9]=="3":
             self.add_rules()
             #del self.content_list[9]

        elif self.content_list[9]=="4":
             self.run_simulation()
             #del self.content_list[9]
        #print(self.content_list[10]) # 2
        if self.content_list[10] =="1":
             self.add_variable()
             #del self.content_list[10]

        elif self.content_list[10] =="2":

             self.add_fuzzy_sets()
             #del self.content_list[10]

        elif self.content_list[10]=="3":
             self.add_rules()
             #del self.content_list[10]

        elif self.content_list[10]=="4":
             self.run_simulation()
             #del self.content_list[10]
        #print(self.content_list[15]) # x
        if  self.content_list[15]=="x":
            self.menue()
            #del self.content_list[15]
        elif self.content_list[15] == "1":
            self.add_variable()
            #del self.content_list[15]
        elif self.content_list[15] == "2":
            self.add_fuzzy_sets()
            #del self.content_list[15]
        elif self.content_list[15] == "3":
            self.add_rules()
            #del self.content_list[15]
        elif self.content_list[15] == "4":
            self.run_simulation()
            #del self.content_list[15]
        #print("/////",self.content_list[16])
        if self.content_list[16] =="1":
             self.add_variable()
             #del self.content_list[16]
        elif self.content_list[16] =="2":
             self.add_fuzzy_sets()
             #del self.content_list[16]
        elif self.content_list[16]=="3":
             self.add_rules()
             #del self.content_list[16]
        elif self.content_list[16]=="4":
             self.run_simulation()
             #del self.content_list[16]
        #print("2222222", self.content_list[22])
        if self.content_list[22]=="x": #third time
            self.menue()
            #del self.content_list[20]

        elif self.content_list[22] == "1":
            self.add_variable()
            #del self.content_list[20]
        elif self.content_list[22] == "2":
            self.add_fuzzy_sets()
            #del self.content_list[20]
        elif self.content_list[22] == "3":
            self.add_rules()
            #del self.content_list[20]
        elif self.content_list[22] == "4":
            self.run_simulation()
            #del self.content_list[20]
        #print("????????",self.content_list[23]) #2
        if  self.content_list[23]=="1":
            self.add_variable()
            #del self.content_list[21]
        elif self.content_list[23] == "2 ":
            self.add_fuzzy_sets()
            #del self.content_list[21]
        elif self.content_list[23] == "3":
            self.add_rules()
            #del self.content_list[21]
        elif self.content_list[23] == "4":
            self.run_simulation()
            #del self.content_list[21]
        ##################################################3
        #print("aaaaaaaaaaaaa",self.content_list[25])
        #print(self.content_list[28])
        if self.content_list[28] == "x":
            self.menue()
            #del self.content_list[25]
        elif self.content_list[28] == "1":
            self.add_variable()
            #del self.content_list[25]
        elif self.content_list[28] == "2":
            self.add_fuzzy_sets()
            #del self.content_list[25]
        elif self.content_list[28] == "3":
            self.add_rules()
            #del self.content_list[25]
        elif self.content_list[28] == "4":
            self.run_simulation()
            #del self.content_list[25]
        ##################################################
        print(self.content_list[29])
        if self.content_list[29] == "1":
            self.add_variable()
            #del self.content_list[25]
        elif self.content_list[29] == "2":
            self.add_fuzzy_sets()
            #del self.content_list[25]
        elif self.content_list[29] == "3 ":
            self.add_rules()
            #del self.content_list[25]
        elif self.content_list[29] == "4":
            self.run_simulation()
            #del self.content_list[25]
        ########################################################
        #print(self.content_list[36]) 4
        if self.content_list[36] == "1":
            self.add_variable()
            #del self.content_list[31]
        elif self.content_list[36] == "2":
            self.add_fuzzy_sets()
            #del self.content_list[31]
        elif self.content_list[36] == "3":
            self.add_rules()
            #del self.content_list[31]
        elif self.content_list[36] == "4 ":
            self.run_simulation()
            #del self.content_list[31]


    def display(self):
        print("Fuzzy Logic Toolbox")
        print("===================")
        print("1- Create a new fuzzy system")
        print("2- Quit")

        if self.variable1=='1':
            self.main_menue()
        else :
            return
b=fuzzy()
b.display()
root = Tk()
root.title("Fuzzy-Logic")
root.geometry("600x600")
root.config(background="#D7CCC8")
photo=ImageTk.PhotoImage(Image.open("C:/Users/Owner/Downloads/fuzzyassigment/fuzzyphoto.jpg"))
mylabel=Label(image=photo)
mylabel.pack()
menubar = Menu(root, background='blue', fg='white')
filemenu = Menu(menubar, background="yellow", tearoff=0)
filemenu.add_command(label="Fuzzification-proj funding", command=b.proi_funding)
filemenu.add_command(label="Fuzzification-exp level", command=b.exp_level)
filemenu.add_command(label="Fuzzification-risk", command=b.risk)
menubar.add_cascade(label="Fuzzification", menu=filemenu)
# --------------------------------------------
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="slope..", command=b.plotting_slop)
filemenu.add_command(label="Slope-constant-TRAP", command=b.plotting_slop_constant_TRAP)
filemenu.add_command(label="Slope-constant-triangle", command=b.plotting_slope_constant_TRA)
filemenu.add_command(label="Slope-variable-TRAP", command=b.plotting_slop)
filemenu.add_command(label="Slope-variable-triangle", command=b.plotting_variable_slop_TRA)
menubar.add_cascade(label="Slope", menu=filemenu)
# --------------------------------------------
# --
filemenu = Menu(menubar, background="yellow", tearoff=0)
# --
filemenu.add_command(label="Plot-Bias-Constant-Trap.", command=b.plotting_bias_constant_trap)
filemenu.add_command(label="Plot-Bias-Constant-Traingular.", command=b.plotting_bias_constant_TRA)
filemenu.add_command(label="Plot-variable-Bias-Trap.", command=b.plotting_bias_TRAP)
filemenu.add_command(label="Plot-variable-Bias-Trap.", command=b.plotting_variable_bias_TRA)

menubar.add_cascade(label="Bias", menu=filemenu)

# ------------------------------------------
filemenu = Menu(menubar, background="yellow", tearoff=0)
#filemenu.add_command(label="Y-Prediction", command=b.plot_inference)

filemenu.add_command(label="defuzzification ", command=b.plot_prediction)
menubar.add_cascade(label="Defuzzifcation ", menu=filemenu)

# --------------------------------------------

filemenu = Menu(menubar, background="yellow", tearoff=0)
filemenu.add_command(label="Plot-Inferance", command=b.plot_inference)
#filemenu.add_command(label="Inferance-Output", command=b.inference)

menubar.add_cascade(label="Inferance", menu=filemenu)
# --------------------------------------------
# --------------------------------------------
filemenu = Menu(menubar, background="yellow", tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit-The-Program", command=root.quit)

menubar.add_cascade(label="Exit", menu=filemenu)
# ---------------------------------------------
root.config(menu=menubar)
root.mainloop()
