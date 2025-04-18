using HTTP
using JSON3
using Random

#Task 1
#simple hello world print
println("Hello, Julia World")

#Task 2
#create static variables
name = "Ian"
age = 22
height = 5.7

#print all the types and values of those variables
println()
println("Type of Name is: $(typeof(name))")
println("Type of age is: $(typeof(age))")
println("Type of height is: $(typeof(height))")
println()
println(name)
println(age)
println(height)


#Task 3
#I got a little ahead of the directions here, but I wanted to try using HTTP requests 
#and fuunctions and didn't realize the function was later in the directions...
println()
#Function that will get a random food from a cool API I found
function get_random_food()
    response = HTTP.get("https://www.themealdb.com/api/json/v1/1/random.php")
    data = JSON3.read(response.body)
    food = data.meals[1].strMeal
    return(food)

end
#Create the list and set a starting point for the number we will be iterating on
favorite_foods = String[]
num = 0

#Loop 6 times to call the api 6 times and add 6 different random foods to out list
while num < 6
    push!(favorite_foods, get_random_food())
    global num += 1
end

println(favorite_foods)

#Task 4
println()
x = rand(Int, 1)
#x in this case will very rarely be 0, but it does work if you manually pu 0 in for x

#iterate over each int in x to find positive
for (int) in (x)
    if int > 0
        println("$x is positive")
    elseif int < 0
        println("$x is negative")
    else
        println("$x is 0")
    end
end

#print each item in favorite_foods list on seperate line
println()
for (food) in (favorite_foods)
    println(food)
end

#Task 5
println()

#Create function to square the input numbers, as well as make sure it is an integer
function print_squared(num)
    if num isa Integer
        num_squared = num * num
        output  = "Square of $num is $num_squared"
    else
        input_type = typeof(num)
        output = "please input a number with type integer instead of $input_type"
    end
    println(output)
end

print_squared(8)

#Task 6
#create function to add 5 years to age
function age_plus_five(current_age)
    new_age  = current_age + 5    
    output = "If you are $current_age now, you will be $new_age in 5 years"
end

#ask for name ang age of User
print("Enter your name here:")
name = readline()

print("Enter your age here:")
age = parse(Int64, readline())

#Print the outputs
println()
println("Hello $name, ")
println(age_plus_five(age))