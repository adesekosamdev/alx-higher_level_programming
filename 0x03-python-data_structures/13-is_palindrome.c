#include "lists.h"

/**
* is_palindrome - checks if a list is a palindrome
* @head: pointer to list to be freed
* Return: 1 if it is a palindrome, 0 if it is not
*/

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *ptr;
	int buffer[1000000];

	len = 0;
	ptr = *head;
	if (ptr == NULL)
		return (1);
	while (ptr)
	{
		buffer[len] = ptr->n;
		ptr = ptr->next;
		len++;
	}

	for (i = 0; i < len; i++)
	{
		if (buffer[i] != buffer[len - i - 1])
			return (0);
	}

	return (1);
}
