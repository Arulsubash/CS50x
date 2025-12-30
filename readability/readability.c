#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int calculate_letters(string letters);
int calculate_words(string words);
int calculate_sentence(string sentence);
int main(void)
{
    string text = get_string("Text: ");
    int letters = calculate_letters(text);
    int words = calculate_words(text);
    int sentence = calculate_sentence(text);
    float L = (float) letters / (float) words * 100;
    float S = (float) sentence / (float) words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 1 && index < 16)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}
int calculate_letters(string letters)
{
    int sum = 0;
    int length = strlen(letters);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(letters[i]))
        {
            sum += 1;
        }
    }
    return sum;
}
int calculate_words(string words)
{
    int sum = 1;
    int length = strlen(words);
    for (int i = 0; i < length; i++)
    {
        if (words[i] == ' ')
        {
            sum += 1;
        }
    }
    return sum;
}
int calculate_sentence(string sentence)
{
    int sum = 0;
    int length = strlen(sentence);
    for (int i = 0; i < length; i++)
    {
        if (sentence[i] == '.' || sentence[i] == '!' || sentence[i] == '?')
        {
            sum += 1;
        }
    }
    return sum;
}
