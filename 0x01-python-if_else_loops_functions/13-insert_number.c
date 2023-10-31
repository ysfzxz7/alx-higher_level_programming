#include "lists.h"

/**
 * insert_node - func that insert a nulber inside  alinked list
 * @head: ptr to the head of the linked list
 * @number: number of the nodes needs to be inserted
 * Return: ptr to the nex linked list otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}

