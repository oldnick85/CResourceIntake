#include <resources.h>

int main(int argc, char *argv[])
{
    printf("res1=");
    for (const auto v : Resources::res1)
    {
        printf("%02X ", v);
    }
    printf("\n");
    printf("res2=");
    for (const auto v : Resources::res2)
    {
        printf("%02X ", v);
    }
    printf("\n");
	return 0;
}
