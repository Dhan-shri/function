def question_list(que_list,opt,solu,lifeline_option,solution):
    # def lifeline(lifeline_option,solution):
    i=0
    k=0
    l=0
    b=0
    while i<len(que_list):
        print(que_list[i])
        j=0
        print("choose one from given option")
        while j<len(opt[k]):
            print(opt[k][j])
            j=j+1
        lifeline=input("Do you want lifeline or not")
        if lifeline=="yes":
            a=0
            while a<len(lifeline_option[l]):
                print(lifeline_option[l][a])
                a=a+1
            choose=input("choose one option from lifeline")
            if choose==solution[b]:
                print("your option is correct, congrats")
            else:
                print("sorry your option is not correct")
            b=b+1
        l=l+1
        k=k+1
        i=i+1


#     return que_list
# def opiton_list(opt):
#     return opt_list
# def solution_list(sol):
#     return sol_list

ques_list=["1. Who is the prime minister of India","2. Which is capital of India", "3. Who is the president of India"]
option_list=[["1.Devendra Fadvanis","2.Narendra Modi","3.Ramnath Kovind","4.Amit Shah"],
            ["1.Delhi","2. Mumbai","3. Kolkata","4. banglore"],
            ["1.Devendra Fadvanis","2.Narendra Modi","3.Ramnath Kovind","4.Amit Shah"]]
sol_list=[2,1,3]
lifeline=[["1. Devendra Fadvanis","2. Narendra Modi"],["1.Delhi","2.Kolkata"],["1. Ramnath Kovind","2. Amit Shah"]]
life_solu=[2,1,1]
question_list(ques_list,option_list,sol_list,lifeline,life_solu)