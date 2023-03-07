#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
* insert_node - inserts  node in a sorted singly linked list
* @head: head of the linked list.
* @number: data in the new node.
*
* Return: address of the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodeNew, *first;

	first = *head;

	nodeNew = malloc(sizeof(listint_t));

	if (nodeNew == NULL)
		return (NULL);

	nodeNew->n = number;
	nodeNew->next = NULL;

	if (*head == NULL || first->n > nodeNew->n)
	{
		nodeNew->next = *head;
		*head = nodeNew;
		return (nodeNew);
	}

	while (first->next != NULL)
	{
		if ((first->next->n > nodeNew->n && first->n < nodeNew->n)
				|| nodeNew->n == first->n)
		{
			nodeNew->next = first->next;
			first->next = nodeNew;
			return (nodeNew);
		}
		first = first->next;
	}
	nodeNew->next = first->next;
	first->next = nodeNew;
	return (nodeNew);
}
