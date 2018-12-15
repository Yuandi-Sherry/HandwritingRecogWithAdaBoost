#ifndef _TRAINIMAGESPARSER_H_
#define _TRAINIMAGESPARSER_H_
#include <iostream>
#include <vector>
#include "CImg.h"
using namespace std;
using namespace cimg_library;
class TrainImagesParser
{
public:
	TrainImagesParser(string filename);
	~TrainImagesParser();
	std::vector<CImg<unsigned char>> getTestImgsSet();
private:
	std::vector<CImg<unsigned char>> testImgsSet;

};
#endif