#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: Python object (string)
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    Py_ssize_t i;
    const char *type;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        fflush(stdout);
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";

    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));

    fflush(stdout);
}

int main(void)
{
    PyObject *p;

    Py_Initialize();

    p = PyUnicode_DecodeUTF8("The spoon does not exist", 24, "strict");
    print_python_string(p);

    p = PyUnicode_DecodeUTF8("ложка не существует", 19, "strict");
    print_python_string(p);

    p = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, "strict");
    print_python_string(p);

    p = PyUnicode_DecodeUTF8("勺子不存在", 5, "strict");
    print_python_string(p);

    p = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, "strict");
    print_python_string(p);

    p = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, "strict");
    print_python_string(p);

    p = PyBytes_FromString("The spoon does not exist");
    print_python_string(p);

    Py_Finalize();
    return 0;
}

