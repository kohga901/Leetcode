#include <string> // for string and to_string()
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int first_digit_int;
        int second_digit_int;
        bool first_digit_existence = false;
        int num1;
        int num2;
        int num3;
        string num3_string;
        ListNode* currentNode = nullptr;
        ListNode* rootNode = nullptr;
        int loop = 1;

        while (l1 != nullptr && l2 != nullptr) {
            cout << "Loop: " << loop << "\n";
            num1 = l1 -> val;
            num2 = l2 -> val;
            num3 = num1 + num2;

            if (first_digit_existence) {
                num3 += first_digit_int;
                first_digit_existence = false;
            }

             // Converting the resulting addition to string.
                num3_string = to_string(num3);

            // If the resulting number has two digits, store the first digit and use the second digit to make a new ListNode object.
            if (num3_string.length() == 2) {
               
                first_digit_existence = true;
                char first_digit = num3_string.at(0);
                char second_digit = num3_string.at(1);

                // Store the first digit.
                first_digit_int = first_digit - '0';

                // Logging.
                cout << "Stored first_digit: " << first_digit_int << "\n";
                cout << "Second_digit: " << second_digit << "\n";
                
                num3 = second_digit - '0';
            }

            // If the resulting addition is a single digit, simply make a new node with the result.

            // If this is the root (first) node, then simply make a new node.
            if (currentNode == nullptr) {
                cout << "Making root node with value: " << num3 << "\n";
                currentNode = new ListNode(num3);
                rootNode = currentNode;
            }
            // Else, make a new node and assign that new node to the pointer of the previously made node.
            else {
                cout << "Making a new node with value: " << num3 << "\n";
                currentNode -> next = new ListNode(num3);
                currentNode = currentNode -> next;
            }

            l1 = l1 -> next;
            l2 = l2 -> next;

            loop++;
        }        

        if (first_digit_existence) {
            currentNode -> next = new ListNode(first_digit_int);
        }

        // If one of the ListNodes is longer than the other, put the remaining integers in the resulting ListNode.
        while (l1 != nullptr) {
            currentNode -> next = new ListNode(l1 -> val);
            currentNode = currentNode -> next;
            l1 = l1 -> next;
        }

        while (l2 != nullptr) {
            currentNode -> next = new ListNode(l2 -> val);
            currentNode = currentNode -> next;
            l2 = l2 -> next;
        }

        return rootNode;

    };
};

int main() {
    Solution sol;
    vector<int> vec1 = {6, 5, 2};
    vector<int> vec2 = {2, 1};

    ListNode* l1 = new ListNode();
    ListNode* ptr1 = l1;
    for (int number : vec1) {
        l1 = new ListNode(number);
        l1 -> next = l1;
    }
    cout << ->val;

    // ListNode* l2 = new ListNode();
    // ListNode* ptr2 = l2;
    // for (int number : vec2) {
    //     if (l2 == nullptr) {
    //         l2 = new ListNode(number);
    //     }
    //     else {
    //     l2 -> val = number;
    //     }
    //     l2 = l2 -> next;
    // }

    // while (ptr1 != nullptr) {
    //     cout << ptr1 -> val;
    //     ptr1 = ptr1 -> next;
    // }
    // while (ptr2 != nullptr) {
    //     cout << ptr2 -> val;
    //     ptr2 = ptr2 -> next;
    // }

    // ListNode* result = sol.addTwoNumbers(l1, l2);

    // string string_result;
    // while (result != nullptr) {
    //     string_result.append(to_string(result -> val));
    //     result = result -> next;
    // }

    // cout << "Result: " << string_result << "\n";

    // delete l1, l1_next, l2, l2_next;
}