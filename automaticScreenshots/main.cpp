#include <iostream>
#include <windows.h>

using namespace std;

// in an hour, every 10 minutes this program will save a screenshot in the default path

int INCREMENT_UPLOAD = 600; // 10 to try
int WINDOW = 3600; // 60 to try

int main()
{
	time_t init_time = time(NULL);
	time_t current_time = init_time;
	int increment = 0;
	
	// it work on a WINDOW seconds long time window
	while (current_time - init_time < WINDOW)
	{
		// upload current time
		time(&current_time);

		// take a screenshot every INCREMENT_UPLOAD seconds 
		if (current_time - init_time > increment)
		{
			keybd_event(VK_LWIN, 0, 0, 0); // Alt press
			keybd_event(VK_SNAPSHOT, 0, 0, 0); // PrntScrn press
			keybd_event(VK_SNAPSHOT, 0, KEYEVENTF_KEYUP, 0); // release
			keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0); // release
			increment += INCREMENT_UPLOAD;
		}
	}
	return 0;
}