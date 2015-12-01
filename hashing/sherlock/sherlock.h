#include <stdio.h>

typedef struct Sig Sig;
struct Sig
{
	int		nval;
	unsigned long	*val;
};

void	init_token_array(void);
Sig * signature(FILE *f);
Sig * signaturep(const char *filepath);