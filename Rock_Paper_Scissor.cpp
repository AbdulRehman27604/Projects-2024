//
//  main.cpp
//  rock paper scissor
//

#include <iostream>
#include <ctime> 
#include <string>
using namespace std;

int userScore = 0;
int botScore = 0;
string game[3] = {"paper", "scissor", "rock"};  

int options() {
    cout << "Please choose between:\n1 - Paper\n2 - Scissors\n3 - Rock";
    int option;
    cout << "\nUser input: ";
    cin >> option;
    return option;
}

int Random() {
    return rand() % 3 + 1;  
}

void score(int user, int bot) {
    if ((user == 2 && bot == 1) || (user == 3 && bot == 2) || (user == 1 && bot == 3)) {
        userScore++;
        cout << "You won this round!\n";
    } else if (user == bot) {
        cout << "It's a draw!\n";
    } else {
        botScore++;
        cout << "Bot won this round!\n";
    }
    cout << "Current Score - You: " << userScore << ", Bot: " << botScore << "\n";
}

void whoWon() {
    if (userScore > botScore) {
        cout << "You won the game!\n";
    } else if (userScore < botScore) {
        cout << "Bot won the game!\n";
    } else {
        cout << "The game is a tie!\n";
    }
}

int main(int argc, const char * argv[]) {
    srand(time(0));  
    
    int rounds = 3;
    for (int i = 0; i < rounds; i++) {
        int userChoice = options();
        
        while (userChoice < 1 || userChoice > 3) {
            cout << "Incorrect option selection. Please retry.\n";
            userChoice = options();
        }
        
        int botChoice = Random();
        
        cout << "You chose: " << game[userChoice - 1] << "\n";
        cout << "Bot chose: " << game[botChoice - 1] << "\n";
        
        score(userChoice, botChoice);
        
        if (userChoice == botChoice) {
            rounds++;  
        }
    }
    
    whoWon();
    
    return 0;
}




