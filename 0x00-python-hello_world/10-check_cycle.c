#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *tempnorm, *tempfwd;

	if (list != NULL)
	{
		tempnorm = list;
		tempfwd = list->next;
		while (tempnorm != NULL && tempfwd != NULL && tempfwd->next != NULL)
		{
			tempnorm = tempnorm->next;
			tempfwd = tempfwd->next->next;
			if (tempnorm == tempfwd)
			return (1);
		}
	}
	return (0);
}
