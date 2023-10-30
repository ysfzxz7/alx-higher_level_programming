#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - func that check if a linked list is a cycle or note
 * @list: ptr to the head of the linked list
 * Return: 0 is cycle otherwise note
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second = list;

	if (list == NULL)
		return (0);

	first = list->next;
	while (first && second && first->next)
	{
		if (first == second)
			return (1);
		first = first->next->next;
		second = second->next;
	}
	return (0);
}

