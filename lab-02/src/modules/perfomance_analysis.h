#pragma once
#include <iostream>
#include <vector>
#include <deque>
#include <chrono>
#include <string>
#include "linked_list.h"

// Анализ и графики
void compare_list_vs_linkedlist();
void compare_list_vs_deque();
void plot_results(const std::string& filename,
                  const std::vector<int>& sizes,
                  const std::vector<double>& times1,
                  const std::vector<double>& times2,
                  const std::string& label1,
                  const std::string& label2,
                  const std::string& title);
