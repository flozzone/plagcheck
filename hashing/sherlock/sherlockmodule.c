#include <Python.h>
#include "sherlock.h"

static PyObject *
sherlock_signature(PyObject *self, PyObject *args)
{
    const char *filepath;
    Sig *ret_sig;

    if (!PyArg_ParseTuple(args, "s", &filepath))
        return NULL;

    ret_sig = signaturep(filepath);

    PyObject* list = PyList_New(0);

    int i = 0;
    while (i < ret_sig->nval) {
        PyObject *val = Py_BuildValue("l", ret_sig->val[i]);
        PyList_Append(list, val);
        i++;
    }

    assert(PyList_Check(list) == 1);

    return list;
}

static PyMethodDef module_methods[] = {
    {"signature",  sherlock_signature, METH_VARARGS,
     "Create a signature from file."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef sherlock =
{
    PyModuleDef_HEAD_INIT,
    "sherlock", /* name of module */
    "Plagiarism detection algorithm",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};

PyMODINIT_FUNC PyInit_sherlock(void)
{
    return PyModule_Create(&sherlock);
}