#include "perfomance_analysis.h"
#include "external/matplotlib-cpp/matplotlibcpp.h"
#include <map>
#include <vector>

namespace plt = matplotlibcpp;

void plot_results(const std::string& title,
                  const std::vector<int>& sizes,
                  const std::vector<double>& times1,
                  const std::vector<double>& times2,
                  const std::string& label1,
                  const std::string& label2,
                  const std::string& filename)
{
    // Преобразуем sizes -> double
    std::vector<double> x(sizes.begin(), sizes.end());

    std::map<std::string, std::string> args1;
    args1["label"] = label1;

    std::map<std::string, std::string> args2;
    args2["label"] = label2;

    plt::figure();
    plt::plot(x, times1, args1);
    plt::plot(x, times2, args2);

    plt::title(title);
    plt::xlabel("List size");
    plt::ylabel("Execution time (ms)");
    plt::legend();
    plt::save(filename);
    plt::close();
}

void compare_list_vs_linkedlist() {
    std::vector<int> sizes = {1000, 2000, 5000, 10000, 20000};
    std::vector<double> ll_times, vec_times;

    for (int N : sizes) {
        LinkedList ll;
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) ll.insert_at_start(i); // O(1)
        auto end = std::chrono::high_resolution_clock::now();
        ll_times.push_back(std::chrono::duration<double>(end - start).count());

        std::vector<int> vec;
        start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) vec.insert(vec.begin(), i); // O(n)
        end = std::chrono::high_resolution_clock::now();
        vec_times.push_back(std::chrono::duration<double>(end - start).count());
    }

    plot_results("list_vs_linkedlist.png", sizes, ll_times, vec_times,
                 "LinkedList", "std::vector (insert at begin)",
                 "Сравнение вставки в начало: LinkedList vs std::vector");
}

void compare_list_vs_deque() {
    std::vector<int> sizes = {1000, 2000, 5000, 10000, 20000};
    std::vector<double> dq_times, vec_times;

    for (int N : sizes) {
        std::deque<int> dq(N, 1);
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) dq.pop_front(); // O(1)
        auto end = std::chrono::high_resolution_clock::now();
        dq_times.push_back(std::chrono::duration<double>(end - start).count());

        std::vector<int> vec(N, 1);
        start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) vec.erase(vec.begin()); // O(n)
        end = std::chrono::high_resolution_clock::now();
        vec_times.push_back(std::chrono::duration<double>(end - start).count());
    }

    plot_results("deque_vs_vector.png", sizes, dq_times, vec_times,
                 "std::deque", "std::vector (erase from begin)",
                 "Сравнение удаления из начала: deque vs vector");
}