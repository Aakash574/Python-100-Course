#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string l = "*";
    for (int i = 0; i < 6; ++i)
    {
        for (int j = 0; j < 6; ++j)
        {
            cout << l;
        }
        cout << "\n";
    }
    return 0;
}
