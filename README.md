# qtpy-screen_adaptive
Non-intrusive window adaptation implemented by Python decorators.

# Problem solved
Qt components and layouts cannot adapt to changes in window size, and the component stretching and sizing strategies provided by Qt are not convenient to use.

This library provides multiple decorators, which can provide solutions for adaptive forms of components, images and text on the basis of convenient and minimal changes to the source code.

# Introduction

## @QTransformation (Not recommand)

This Python decorator causes components to scale according to the scale of the form, but it also inevitably causes deformation.

## @QKeepAspectRatio

This Python decorator allows components to scale according to the form scaling ratio while maintaining the original aspect ratio, but only for the widget itself, not for the content.

## @QTextAdaptive

This Python decorator complements the @QKeepAspectRatio decorator for text content, supporting rich text widgets such as QLabel.

## @QImageAdative

This Python decorator is a supplement to the @QKeepAspectRatio decorator for image content, mainly supporting QPixmap objects

# How to use

All Python decorators in the QScreenAdaptive file are class decorators, which means that you need to use the QWidget class or its subclasses.

Example:
```python
from QScreenAdaptive import QKeepAspectRatio, QTextAdaptive, QImageAdaptive

@QKeepAspectRatio
@QTextAdaptive
@QImageAdaptive
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
```

For a complete example, please see `demo.py`.
