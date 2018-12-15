#ifndef _TRAINLABELSPARSER_H_
#define _TRAINLABELSPARSER_H_
#include <iostream>
#include <vector>
#include "CImg.h"
using namespace std;
using namespace cimg_library;
class TrainLabelsParser
{
public:
	TrainLabelsParser(string filename);
	~TrainLabelsParser();
	std::vector<int> getTestLabelsSet();
private:
	std::vector<int> testLabelsSet;

};
#endif