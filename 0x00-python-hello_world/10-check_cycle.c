#include "lists.h"
#include "stdio.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the list
 *
 * Return: 0 if no cycle, 1 if cycle is found
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow)
				return (1);
		}
		else
			return (0);
	}
}
