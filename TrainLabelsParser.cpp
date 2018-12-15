#include <iostream>
#include <fstream>
#include "TrainLabelsParser.h"
#include "CImg.h"
using namespace std;
using namespace cimg_library;
TrainLabelsParser::TrainLabelsParser(string filename) {
	ifstream inFile(filename.c_str(), ios::in|ios::binary);
	if(!inFile) {
		cout << "There's something error when openning the file. " << endl;
	} else {
		char onChar[1];
		for(int i = 0; i < 4; i++) {
			// 读取第一个32bit magic number
			inFile.read((char*)onChar, sizeof(char));
		}
		unsigned char num[4];
		for(int i = 0; i < 4; i++) {
			inFile.read((char*)(num+i), sizeof(char));
		}
		// 标签总数
		int numOfLabels = num[0] * pow(16,6) + num[1] * pow(16,4) + num[2] * pow(16,2) + num[3];
		// 读取每个标签
		for(int i = 0; i < numOfLabels; i++) {
			unsigned char label[1];
			inFile.read((char*)label, sizeof(char));
			testLabelsSet.push_back((int)*label);
		}
	}
}
TrainLabelsParser::~TrainLabelsParser() {

}

std::vector<int> TrainLabelsParser::getTestLabelsSet() {
	for(int i = 0; i < testLabelsSet.size(); i++) {
		cout << testLabelsSet[i] << " ";
	}
	return testLabelsSet;
}