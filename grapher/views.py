# grapher/views.py

from django.shortcuts import render
from chartjs.views.lines import BaseLineChartView
from scraper.models import ScrapedData

class ScrapedDataChartView(BaseLineChartView):
    model = ScrapedData
    date_field = 'timestamp'
    percentage_field = 'percentage'
    count_pool_field = 'count_pool'
    count_aquapark_field = 'count_aquapark'

    def get_labels(self):
        return [str(entry.timestamp) for entry in ScrapedData.objects.all()]

    def get_data(self):
        data = {
            'labels': self.get_labels(),
            'datasets': [
                {
                    'label': 'Percentage',
                    'data': [entry.percentage for entry in ScrapedData.objects.all()],
                },
                {
                    'label': 'Count Pool',
                    'data': [entry.count_pool for entry in ScrapedData.objects.all()],
                },
                {
                    'label': 'Count Aquapark',
                    'data': [entry.count_aquapark for entry in ScrapedData.objects.all()],
                },
            ],
        }
        return data

    def get_options(self):
        options = {
            'responsive': True,
            'title': {
                'display': True,
                'text': 'Scraped Data Over Time',
            },
            'scales': {
                'xAxes': [
                    {
                        'type': 'time',
                        'time': {
                            'unit': 'day',
                        },
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Timestamp',
                        },
                    },
                ],
                'yAxes': [
                    {
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Value',
                        },
                    },
                ],
            },
        }
        return options

def chart_view(request):
    return render(request, './chart.html', {'chart': ScrapedDataChartView()})