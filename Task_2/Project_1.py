movies = [
    ("3 Idiots", 55000000),
    ("PK", 85000000),
    ("Dangal", 70000000),
    ("Bajrangi Bhaijaan", 90000000),
    ("Padmaavat", 215000000),
    ("War", 150000000),
    ("Brahmastra: Part One – Shiva", 410000000)
]

enter_movie=[]
def add_movies():
    try:
        count = int(input("How many movies do you want to add? "))
        for _ in range(count):
            name = input("Enter movie name: ")
            budget = int(input("Enter movie budget: "))
            enter_movie.append((name, budget))
    except ValueError:
        print("Invalid input! Please enter a number.")

def avg():
    data=enter_movie if enter_movie else movies
    avg=sum(i[1] for i in data)/len(data)
    print("The avg cost of movies is: ",avg)
    total_movies=0
    for i in data:
        if i[1]>avg:
            total_movies+=1
            diff=i[1]-avg
            print(i[0])
            print(f"The budget is higher then avg is {diff}")
    if total_movies > 0:
        print(f"{avg}These movies have high budget then avg cost.")
        print(f"The count of movies have high budget then avg is {total_movies}")
    else:
        print("No movie has higher budget than avg")
   
print("Note: Some Bollywood movies are already added for testing. You can also add your own movies.")
print("1: Add a new movie")
print("2: To display basic info")
while True:
    option=int(input("Chose a option:"))
    if option==1:
        add_movies()
    elif option==2:
        avg()
    elif option==3:
        break
    else:
        print("Invalid input!Try again.")