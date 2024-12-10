#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void filter_subtractions(const char *input_file, const char *output_file) {
    FILE *infile = fopen(input_file, "r");
    FILE *outfile = fopen(output_file, "w");

    if (infile == NULL) {
        printf("Error opening input file.\n");
        return;
    }

    if (outfile == NULL) {
        printf("Error opening output file.\n");
        fclose(infile);
        return;
    }

    char line[256];

    while (fgets(line, sizeof(line), infile)) {
        printf("Reading line: %s\n", line);  

        char operation[10];
        int num1, num2;
        
        int result = sscanf(line, "%9[^,],%d-%d", operation, &num1, &num2);
        
        printf("sscanf result: %d\n", result); 
        
        if (result == 3) {
            printf("Parsed: operation = %s, num1 = %d, num2 = %d\n", operation, num1, num2);

            if (num1 < 21 && num2 >= 0 && num2 <= 9) {
                fputs(line, outfile);
                printf("Line written to output file.\n");
            } else {
                printf("Filtering out: num1 = %d, num2 = %d\n", num1, num2);  
            }
        } else {
            printf("sscanf failed to parse the line.\n");
        }
    }

    fclose(infile);
    fclose(outfile);
    printf("Filtered data saved to %s\n", output_file);
}
int main() {
    const char *input_file = "C:/Users/Condor/Documents/GitHub/AP/tryfiles/input.txt";
    const char *output_file = "filtered_file.txt"; 

    filter_subtractions(input_file, output_file);

    return 0;
}
