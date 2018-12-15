#include <iostream>
#include "TrainImagesParser.h"
#include "CImg.h"
using namespace std;
using namespace cimg_library;

int main() {
	string filename = "testSet/train-images.idx3-ubyte";
	TrainImagesParser trainImageParser(filename);
	trainImageParser.getTestImgsSet();
}