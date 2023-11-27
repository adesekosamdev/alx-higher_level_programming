#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tempnorm, *tempfwd;

	if (list != NULL)
	{
		tempnorm = list;
		tempfwd = list->next;
		while (tempnorm != NULL && tempfwd != NULL && tempfwd->next != NULL)
		{
			if (tempnorm == tempfwd)
			return (1);
		}
		tempnorm = tempnorm->next;
		tempfwd = tempfwd->next->next;
	}
	return (0);
}
