from PyQt5.QtGui import QResizeEvent, QPixmap
from PyQt5.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout


def QTransformation(origin_cls):
    super_class = origin_cls.mro()[1]

    class QTransformationWidget:
        def __new__(cls, *args, **kwargs):
            instance = origin_cls.__new__(origin_cls, *args, **kwargs)
            super_class.__init__(instance)
            if not hasattr(instance, '__inited'):
                setattr(instance, '__inited', True)
                instance.__init__(*args, **kwargs)

            originalResizeEvent = instance.resizeEvent

            def resizeEvent(event: QResizeEvent) -> None:
                originalResizeEvent(event)

                if not hasattr(instance, 'init_size'):
                    instance.init_size = instance.size()

                width_ratio = instance.size().width() / instance.init_size.width()
                height_ratio = instance.size().height() / instance.init_size.height()

                for child in instance.children():
                    if isinstance(child, QLayout):
                        if not hasattr(child, 'init_margin'):
                            child.init_margin = child.contentsMargins()

                        if not hasattr(child, 'init_spacing'):
                            child.init_spacing = child.spacing()

                        content_margins = child.contentsMargins()
                        content_margins.setRight(int(child.init_margin.right() * width_ratio / 2))
                        content_margins.setLeft(int(child.init_margin.left() * width_ratio / 2))
                        content_margins.setTop(int(child.init_margin.top() * height_ratio / 2))
                        content_margins.setBottom(int(child.init_margin.bottom() * height_ratio / 2))
                        child.setContentsMargins(content_margins)

                        if isinstance(child, QHBoxLayout):
                            child.setSpacing(int(child.init_spacing * width_ratio))
                        elif isinstance(child, QVBoxLayout):
                            child.setSpacing(int(child.init_spacing * height_ratio))
                        else:
                            child.setSpacing(int(child.init_spacing * (width_ratio + height_ratio) / 2))

                    if hasattr(child, 'size'):
                        if not hasattr(child, 'init_size'):
                            child.init_size = child.size()
                        else:
                            child.setFixedWidth(int(child.init_size.width() * width_ratio))
                            child.setFixedHeight(int(child.init_size.height() * height_ratio))

            instance.resizeEvent = resizeEvent

            return instance

    return QTransformationWidget


def QKeepAspectRatio(origin_cls):
    super_class = origin_cls.mro()[1]

    class QKeepAspectRatioWidget:
        def __new__(cls, *args, **kwargs):
            instance = origin_cls.__new__(origin_cls, *args, **kwargs)
            super_class.__init__(instance)
            if not hasattr(instance, '__inited'):
                setattr(instance, '__inited', True)
                instance.__init__(*args, **kwargs)

            originalResizeEvent = instance.resizeEvent

            def resizeEvent(event: QResizeEvent) -> None:
                originalResizeEvent(event)
                if not hasattr(instance, 'init_size'):
                    instance.init_size = instance.size()

                width_ratio = instance.size().width() / instance.init_size.width()
                height_ratio = instance.size().height() / instance.init_size.height()
                ratio = min(width_ratio, height_ratio)

                for child in instance.children():
                    if isinstance(child, QLayout):
                        if not hasattr(child, 'init_margin'):
                            child.init_margin = child.contentsMargins()

                        if not hasattr(child, 'init_spacing'):
                            child.init_spacing = child.spacing()

                        content_margins = child.contentsMargins()
                        content_margins.setRight(int(child.init_margin.right() * ratio / 2))
                        content_margins.setLeft(int(child.init_margin.left() * ratio / 2))
                        content_margins.setTop(int(child.init_margin.top() * ratio / 2))
                        content_margins.setBottom(int(child.init_margin.bottom() * ratio / 2))
                        child.setContentsMargins(content_margins)

                        if isinstance(child, QHBoxLayout):
                            child.setSpacing(int(child.init_spacing * width_ratio))
                        elif isinstance(child, QVBoxLayout):
                            child.setSpacing(int(child.init_spacing * height_ratio))
                        else:
                            child.setSpacing(int(child.init_spacing * ratio))

                    if hasattr(child, 'size'):
                        if not hasattr(child, 'init_size'):
                            child.init_size = child.size()
                        else:
                            child.setFixedWidth(int(child.init_size.width() * ratio))
                            child.setFixedHeight(int(child.init_size.height() * ratio))

            instance.resizeEvent = resizeEvent
            return instance

    return QKeepAspectRatioWidget


def QTextAdaptive(origin_cls):
    super_class = origin_cls.mro()[1]

    class QTextAdaptiveWidget:
        def __new__(cls, *args, **kwargs):
            instance = origin_cls.__new__(origin_cls, *args, **kwargs)
            super_class.__init__(instance)
            if not hasattr(instance, '__inited'):
                setattr(instance, '__inited', True)
                instance.__init__(*args, **kwargs)

            originalResizeEvent = instance.resizeEvent

            def resizeEvent(event: QResizeEvent) -> None:
                originalResizeEvent(event)

                if not hasattr(instance, 'init_size'):
                    instance.init_size = instance.size()

                width_ratio = instance.width() / instance.init_size.width()
                height_ratio = instance.height() / instance.init_size.height()
                ratio = min(width_ratio, height_ratio)

                def for_each(parent):
                    for child in parent.children():
                        if hasattr(child, 'text'):
                            if not hasattr(child, 'init_font'):
                                font = child.font()
                                if font.pixelSize() == -1:
                                    font.setPixelSize(15)
                                child.init_font = font
                            font = child.font()
                            pixel_size = int(child.init_font.pixelSize() * ratio)
                            font.setPixelSize(pixel_size)
                            child.setFont(font)

                        for_each(child)

                for_each(instance)

            instance.resizeEvent = resizeEvent

            return instance

    return QTextAdaptiveWidget


def QImageAdaptive(origin_cls):
    super_class = origin_cls.mro()[1]

    class QImageAdaptiveWidget:
        def __new__(cls, *args, **kwargs):
            instance = origin_cls.__new__(origin_cls, *args, **kwargs)
            super_class.__init__(instance)
            if not hasattr(instance, '__inited'):
                setattr(instance, '__inited', True)
                instance.__init__(*args, **kwargs)

            originalResizeEvent = instance.resizeEvent

            def resizeEvent(event: QResizeEvent) -> None:
                originalResizeEvent(event)

                if not hasattr(instance, 'init_size'):
                    instance.init_size = instance.size()

                width_ratio = instance.width() / instance.init_size.width()
                height_ratio = instance.height() / instance.init_size.height()
                ratio = min(width_ratio, height_ratio)

                def for_each(parent):
                    for child in parent.children():
                        if hasattr(child, 'pixmap'):
                            if not child.pixmap():
                                continue

                            if not hasattr(child, 'init_pixmap'):
                                child.init_pixmap = QPixmap(child.pixmap())

                            pixmap = child.init_pixmap.scaled(int(child.init_pixmap.size().width()*ratio),int(child.init_pixmap.size().height()*ratio))
                            child.setPixmap(pixmap)
                        for_each(child)

                for_each(instance)
            instance.resizeEvent = resizeEvent

            return instance
    return QImageAdaptiveWidget
