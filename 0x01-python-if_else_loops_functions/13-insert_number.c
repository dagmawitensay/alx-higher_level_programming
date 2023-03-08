#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a node into a sorted
 * linked list
 * @head: pointer to the head of the list
 * @number: value to be inserted
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *forward;

	current = *head;
	forward = current->next;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	while (forward->next)
	{
		if (forward->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = forward;
		forward = forward->next;
	}
	return (new);
}
