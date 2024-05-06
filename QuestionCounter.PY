import pandas as pd


def Show_Question_Percentage():
    Question_Percentage = pd.read_csv("Question_Percentage.csv")
    Question_Percentage_DF = pd.DataFrame(Question_Percentage)
    print(Question_Percentage_DF) 

def add_new_questions():
    Question_Percentage = pd.read_csv("Question_Percentage.csv")
    materia = input("digite qual a materia das Questoes")
    conteudo = input("digite o conteudo dessas questoes")
    questoes = input("digite quantas questões foram feitas")
    questao_errada = input("digite quantas questões voce errou")
    taxa = int((int(questao_errada)/int(questoes))*100)
    df2 = {"materia": materia,"conteudo": conteudo,"numero de questoes":questoes,"taxa de erro":f'{taxa}%', "qnt de erros":questao_errada }
    Question_Percentage_DF = pd.DataFrame(Question_Percentage)
    df = Question_Percentage_DF._append(df2,ignore_index=True)
    df.to_csv("Question_percentage.csv",index=False)
    print("Questões Atualizadas")

def show_total_questions():
    Questions = pd.read_csv("Questions.csv")
    questions_DF = pd.DataFrame(Questions)
    print(questions_DF)

def update_Questions():
    Question_Percentage = pd.read_csv("Question_percentage.csv")
    Question_Percentage_df= pd.DataFrame(Question_Percentage,columns=["materia","conteudo","questoes","taxa de erro","Qnt de erros"])
    conteudo_desejado= input("qual nome do conteudo que voce deseja atualizar")
    for i in range(len(Question_Percentage_df)):
        print(Question_Percentage_df.loc[i,"conteudo"])
        if (Question_Percentage_df.loc[i,"conteudo"]==conteudo_desejado):
            number_of_questions = Question_Percentage_df.loc[i,"questoes"]
            number_of_misses =  Question_Percentage_df.loc[i,"Qnt de erros"]
            number_of_misses = number_of_misses
            number_of_questions = number_of_questions
            new_questions = input("quantas novas questões voce fez")
            new_misses = input("quantos novos erros voce fez")
            number_of_questions += int(new_questions)
            number_of_misses+= int(new_misses)
            new_percentage = (number_of_misses/number_of_questions)*100
            new_percentage = round(new_percentage,1)
            Question_Percentage_df.loc[i,"questoes"] = number_of_questions
            Question_Percentage_df.loc[i,"Qnt de erros"] = number_of_misses
            Question_Percentage_df.loc[i,"materia"] = f"{new_percentage}%"
            print("questoes atualizadas")
            

update_Questions()
Show_Question_Percentage()