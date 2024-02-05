#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>

int main()
{
    FILE *fptr;
    int bytesRead = 0;
    uint8_t buf[50];
    fptr = fopen ("D:\\FORMFILLINGMAIN\\NFC_Web_Portal\\","rb");  // open file in binary mode
    if (fptr)
    {
        while (!feof(fptr))
         {
           bytesRead += fread (buf,1,40,fptr);
         }
        fclose (fptr);                       //;
        printf ("Total bytes read = %d\n",bytesRead);
    }
    else
      printf("File open error\n");
    return 0;
}