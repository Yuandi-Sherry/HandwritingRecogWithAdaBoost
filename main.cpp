#include <iostream>
#include "TrainImagesParser.h"
#include "TrainLabelsParser.h"
#include "CImg.h"
using namespace std;
using namespace cimg_library;

int main() {
	string filename = "testSet/train-images.idx3-ubyte";
	TrainImagesParser trainImageParser(filename);
	trainImageParser.getTestImgsSet();
	filename = "testSet/train-labels.idx1-ubyte";
	TrainLabelsParser trainLabelsParser(filename);
	trainLabelsParser.getTestLabelsSet();
}