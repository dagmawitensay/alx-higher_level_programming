#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if a linked
 * list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *start;
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *temp;

	fast = *head;
	slow = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	prev = NULL;
	while (slow)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	
	start = *head;	 
	while (prev)
	{
		if (start->n != prev->n)
		{
			return (0);
		}
		start = start->next;
		prev = prev->next;
	}
	return (1);
}
