#include <iostream>
#include <fstream>
#include "TrainImagesParser.h"
#include "CImg.h"
using namespace std;
using namespace cimg_library;
TrainImagesParser::TrainImagesParser(string filename) {
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
		// 图片总数
		int numOfImgs = num[0] * pow(16,6) + num[1] * pow(16,4) + num[2] * pow(16,2) + num[3];
		// cout << numOfImgs << endl;
		// 读取长和宽
		unsigned char temp[4];
		for(int j = 0; j < 4; j++) {
			inFile.read((char*)(temp+j), sizeof(char));
		}
		int numOfRows = temp[0] * pow(16,6) + temp[1] * pow(16,4) + temp[2] * pow(16,2) + temp[3];
		// cout << "number of rows " << numOfRows << endl;
		for(int j = 0; j < 4; j++) {
			inFile.read((char*)(temp+j), sizeof(char));
		}
		int numOfCols = temp[0] * pow(16,6) + temp[1] * pow(16,4) + temp[2] * pow(16,2) + temp[3];
		// cout << "number of cols " << numOfCols << endl;
		// 读取每个像素
		CImg<unsigned char> * imgBuffer;
		for(int i = 0; i < numOfImgs; i++) {
			imgBuffer = new CImg<unsigned char>(numOfCols, numOfRows, 1, 1);
			unsigned char pixel[1];
			for(int j = 0; j < numOfRows; j++) {
				for(int k = 0; k < numOfCols; k++) {
					inFile.read((char*)pixel, sizeof(char));
					(*imgBuffer)(k,j,0,0) = pixel[0];
				}
			}
			// imgBuffer -> display();
			// imgBuffer -> save("temp.bmp");
			testImgsSet.push_back(*imgBuffer);
			delete imgBuffer;
		}
	}
}
TrainImagesParser::~TrainImagesParser() {

}

std::vector<CImg<unsigned char>> TrainImagesParser::getTestImgsSet() {
	for(int i = 0; i < testImgsSet.size(); i++) {
		testImgsSet[i].display();
	}
	return testImgsSet;
}