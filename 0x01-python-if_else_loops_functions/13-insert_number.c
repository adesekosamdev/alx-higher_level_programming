#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pointer to the head of the linked list.
 * @number: number to insert.
 * Return: NULL if function fails
 *         Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new_node;

	node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
