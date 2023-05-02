#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
    cout << "count of argc" << argc << endl;
    for (int i = 0; i < 3; i++){
        cout << "value at "<< i << argv[i] << endl;
    }
    if (argc == 1 || argc > 2) {
        cout << "Invalid number of arguments" << endl;
        return EXIT_FAILURE;
    }
    if (argc == 2) {
        if (remove(argv[1]) != 0) {
            cout << "Error deleting file" << endl;
            return EXIT_FAILURE;
        } else {
            cout << "File deleted successfully" << endl;
            return EXIT_SUCCESS;
        }
    }
    if (argc == 3) {
        if (rename(argv[1], argv[2]) != 0) {
            cout << "Error moving file" << endl;
            return EXIT_FAILURE;
        } else {
            cout << "File moved successfully" << endl;
            return EXIT_SUCCESS;
        }
    }
}
