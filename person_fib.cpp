#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
	private:
		int age;
		int fibbonacci(int n)
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}
int Person::fib(){
    return fibonacci(age);
    }
int Person::fibonacci(int n){
    if (n <= 1)
       return n;
    else
       return fibonacci(n-1) + fibonacci(n-2);
    }


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}