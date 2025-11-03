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