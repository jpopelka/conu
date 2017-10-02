"""
Abstract definition for an Image
"""


class Image(object):
    """
    A class which represents an arbitrary container image. It contains utility methods
    to manipulate it.
    """

    def mount_image(self, mount_point=None):
        """
        mount an image to host system
        :param mount_point: str, mount_point on host system
        :return: mount_point
        """
        raise NotImplementedError("mount_image method is not implemented")

    def file_is_present(self, file_path):
        """
        check if file 'file_path' is present in container

        :param file_path: str, path to the file
        :return: True if file exists, False if file does not exist
        """
        raise NotImplementedError("get_file method is not implemented")

    def directory_is_present(self, directory_name):
        """
        check if directory 'directory_name' is present in container

        :param directory_name: str, Directory to check
        :return: True if directory exists, False if directory does not exist
        """
        raise NotImplementedError("directory_is_present is not implemented")

    def get_selinux_context(self, file_path):
        """
        return a permissions for 'file_path'
        :param file_path: str, path to the file
        :return: str
        """

        raise NotImplementedError("get_selinux_context is not implemented")


class S2Image(Image):
    """
    Additional functionality related to s2i-enabled container images
    """

    def extend(self, source, new_image_name=None, s2i_args=None):
        """
        extend this s2i-enabled image using provided source, raises ConuException if
        `s2i build` fails

        :param source: str, source used to extend the image, can be path or url
        :param new_image_name: str, name of the new, extended image
        :param s2i_args: list of str, additional args provided to `s2i build`
        :return: S2Image instance
        """
        raise NotImplementedError("extend method is not implemented")

    def usage(self):
        """
        Provide output of `s2i usage`

        :return: str
        """
        raise NotImplementedError("usage method is not implemented")