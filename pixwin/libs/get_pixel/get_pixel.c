#include <Python.h>
#include <Windows.h>

COLORREF get_pixel(PyObject *args) {
    PyObject *hdc_object;
    int x;
    int y;
    
    if (!PyArg_ParseTuple(args, "Oii", &hdc_object, &x, &y)) return NULL;

    const HDC hdc = PyLong_AsVoidPtr(hdc_object);
    return GetPixel(hdc, x, y);
}

static PyObject* get_rgb(PyObject *self, PyObject *args) {
    const COLORREF colour = get_pixel(args);
    return Py_BuildValue("(iii)", colour & 0xff, (colour >> 8) & 0xff, (colour >> 16) & 0xff);
}

static PyObject* get_red_value(PyObject *self, PyObject *args) {
    return Py_BuildValue("i", get_pixel(args) & 0xff);
}

static PyObject* get_green_value(PyObject *self, PyObject *args) {
    return Py_BuildValue("i", (get_pixel(args) >> 8) & 0xff);
}

static PyObject* get_blue_value(PyObject *self, PyObject *args) {
    return Py_BuildValue("i", (get_pixel(args) >> 16) & 0xff);
}

static PyMethodDef get_pixel_methods[] = {
    {"get_rgb",         get_rgb,         METH_VARARGS, "Get RGB value of pixel"},
    {"get_red_value",   get_red_value,   METH_VARARGS, "Get red value of pixel"},
    {"get_green_value", get_green_value, METH_VARARGS, "Get green value of pixel"},
    {"get_blue_value",  get_blue_value,  METH_VARARGS, "Get blue value of pixel"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef get_pixel_module = {
    PyModuleDef_HEAD_INIT,
    "get_pixel",
    "get_pixel module",
    -1,
    get_pixel_methods
};

PyMODINIT_FUNC PyInit_get_pixel() {
    return PyModule_Create(&get_pixel_module);
}
