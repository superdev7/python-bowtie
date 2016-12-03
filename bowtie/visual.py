# -*- coding: utf-8 -*-
"""
Visual components
"""

from bowtie._component import Component, jdumps
from bowtie._progress import Progress


# pylint: disable=too-few-public-methods
class _Visual(Component):
    """
    Used to test if a an object is a controller.
    All controllers must inherit this class.
    """
    def __init__(self, progress_color):
        progress_args = {}
        if progress_color:
            progress_args['color'] = progress_color
        self.progress = Progress(**progress_args)
        super(_Visual, self).__init__()


class SmartGrid(_Visual):
    """Table Component with filtering and sorting

    Parameters
    ----------
    columns : list, optional
        List of column names to display.
    results_per_page : int, optional
        Number of rows on each pagination of the table.

    """
    _TEMPLATE = 'griddle.jsx'
    _COMPONENT = 'SmartGrid'
    _PACKAGE = 'griddle-react'
    _TAG = ('<SmartGrid '
            'socket={{socket}} '
            'uuid={{{uuid}}} '
            'columns={{{columns}}} '
            'resultsPerPage={{{results_per_page}}}'
            '/>')

    def __init__(self, columns=None, results_per_page=10,
                 progress_color=None):
        if columns is None:
            columns = []
        self.columns = columns
        self.results_per_page = results_per_page
        super(SmartGrid, self).__init__(progress_color=progress_color)

    def _instantiate(self):
        return self._TAG.format(
            uuid="'{}'".format(self._uuid),
            columns=jdumps(self.columns),
            results_per_page=self.results_per_page
        )

    # pylint: disable=no-self-use
    def do_update(self, data):
        """Updates the data of the table

        Parameters
        ----------
        data : list of dicts
            Each entry in the list must be a dict
            with the same keys which are the columns
            of the table.

        Returns
        -------
        None

        """
        return data


# These visuals are partially implemented
#
# class FixedTable(_Visual):
#     _TEMPLATE = 'fixedtable.jsx'
#     _COMPONENT = 'FixedTable'
#     _PACKAGE = 'fixed-data-table'
#     _TAG = ('<FixedTable '
#            'socket={{socket}} '
#            'uuid={{{uuid}}} '
#            'rows={{{rows}}} '
#            'columns={{{columns}}} '
#            '/>')
#
#     def __init__(self):
#         super(FixedTable, self).__init__()
#
#     def _instantiate(self, columns, rows):
#         return self._TAG.format(
#             uuid="'{}'".format(self._uuid),
#             rows=rows,
#             columns=columns
#         )
#
#
# class DataTable(_Visual):
#     _TEMPLATE = 'datatables.jsx'
#     _COMPONENT = 'JTable'
#     _PACKAGE = 'react-jquery-datatables'
#     _TAG = ('<JTable '
#            'socket={{socket}} '
#            'uuid={{{uuid}}} '
#            '/>')
#
#     def __init__(self):
#         super(DataTable, self).__init__()
#
#     def _instantiate(self, columns, rows):
#         return self._TAG.format(
#             uuid="'{}'".format(self._uuid),
#         )
#
#
# class Grid(_Visual):
#     _TEMPLATE = 'dazzlegrid.jsx'
#     _COMPONENT = 'Grid'
#     _PACKAGE = 'react-data-grid'
#     _TAG = ('<Grid '
#            'socket={{socket}} '
#            'uuid={{{uuid}}} '
#            '/>')
#
#     def __init__(self):
#         super(Grid, self).__init__()
#
#     def _instantiate(self, columns, rows):
#         return self._TAG.format(
#             uuid="'{}'".format(self._uuid),
#         )
#
#
# class Table(_Visual):
#     _TEMPLATE = 'datagrid.jsx'
#     _COMPONENT = 'Table'
#     _PACKAGE = 'react-datagrid'
#     _TAG = ('<Table '
#            'socket={{socket}} '
#            'uuid={{{uuid}}} '
#            '/>')
#
#     def __init__(self):
#         super(Table, self).__init__()
#
#     def _instantiate(self, columns, rows):
#         return self._TAG.format(
#             uuid="'{}'".format(self._uuid),
#         )


class Plotly(_Visual):
    """
    Plotly component.
    """
    _TEMPLATE = 'plotly.jsx'
    _COMPONENT = 'PlotlyPlot'
    _PACKAGE = 'plotly.js'
    _TAG = ('<PlotlyPlot initState={{{init}}} '
            'socket={{socket}} '
            'uuid={{{uuid}}} '
            '/>')

    def __init__(self, init=None, progress_color=None):
        if init is None:
            init = dict(data=[], layout={'autosize': False})
        self.init = init
        super(Plotly, self).__init__(progress_color=progress_color)

    def _instantiate(self):
        return self._TAG.format(
            uuid="'{}'".format(self._uuid),
            init=jdumps(self.init),
        )


    ## Events

    def on_click(self):
        """Plotly click event.

        | **Payload:** TODO.

        Returns
        -------
        str
            Name of event.

        """
        pass

    def on_beforehover(self):
        """Emits an event before hovering over a point.

        | **Payload:** TODO.

        Returns
        -------
        str
            Name of event.

        """
        pass

    def on_hover(self):
        """Emits an event after hovering over a point.

        | **Payload:** TODO.

        Returns
        -------
        str
            Name of event.

        """
        pass

    def on_unhover(self):
        """Emits an event when hover is removed.

        | **Payload:** TODO.

        Returns
        -------
        str
            Name of event.

        """
        pass

    def on_select(self):
        """Emits an event when points are selected with a tool.

        | **Payload:** TODO.

        Returns
        -------
        str
            Name of event.

        """
        pass

    ## Commands

    # pylint: disable=no-self-use
    def do_all(self, plot):
        """Replaces the entire plot.

        Parameters
        ----------
        plot : dict
            Dict that can be plotted with Plotly.

        Returns
        -------
        None

        """
        return plot

    def do_data(self, data):
        """Replaces the data portion of the plot.

        Parameters
        ----------
        data : list of traces
            List of data to replace the old data.

        Returns
        -------
        None

        """
        return data

    def do_layout(self, layout):
        """Updates the layout.

        Parameters
        ----------
        layout : dict
            Contains layout information.

        Returns
        -------
        None

        """
        return layout

    def do_config(self, config):
        """Updates the configuration of the plot.

        Parameters
        ----------
        config : dict
            Plotly config information.

        Returns
        -------
        None

        """
        return config
