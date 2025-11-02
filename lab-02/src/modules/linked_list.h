#pragma once
#include <iostream>

struct Node {
    int data;               // O(1)
    Node* next;             // O(1)
    Node(int val) : data(val), next(nullptr) {} // O(1)
};

class LinkedList {
private:
    Node* head;  // O(1)
    Node* tail;  // O(1)
public:
    LinkedList();                        // O(1)
    ~LinkedList();                       // O(n)
    void insert_at_start(int value);     // O(1)
    void insert_at_end(int value);       // O(1)
    void delete_from_start();            // O(1)
    void traversal();                    // O(n)
};
