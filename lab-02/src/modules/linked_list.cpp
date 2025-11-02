#include "linked_list.h"

LinkedList::LinkedList() : head(nullptr), tail(nullptr) {} // O(1)

LinkedList::~LinkedList() { // O(n)
    Node* current = head;
    while (current) {               // O(n)
        Node* temp = current;       // O(1)
        current = current->next;    // O(1)
        delete temp;                // O(1)
    }
}

void LinkedList::insert_at_start(int value) { // O(1)
    Node* newNode = new Node(value); // O(1)
    newNode->next = head;            // O(1)
    head = newNode;                  // O(1)
    if (!tail) tail = newNode;       // O(1)
}

void LinkedList::insert_at_end(int value) { // O(1)
    Node* newNode = new Node(value); // O(1)
    if (!head) {                     // O(1)
        head = tail = newNode;       // O(1)
        return;
    }
    tail->next = newNode;            // O(1)
    tail = newNode;                  // O(1)
}

void LinkedList::delete_from_start() { // O(1)
    if (!head) return;                 // O(1)
    Node* temp = head;                 // O(1)
    head = head->next;                 // O(1)
    delete temp;                       // O(1)
    if (!head) tail = nullptr;         // O(1)
}

void LinkedList::traversal() { // O(n)
    Node* current = head;
    while (current) {              // O(n)
        std::cout << current->data << " "; // O(1)
        current = current->next;           // O(1)
    }
    std::cout << std::endl; // O(1)
}
