from html.parser import HTMLParser

import numpy as np
import pandas as pd


class DistTableHTMLParser(HTMLParser):
	def __init__(self, html_file, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# numerical data
		self.data_output = []
		# set_ids
		self.set_ids = []

		self.load_html(html_file)

	def load_html(self, file):
		with open(file, 'r') as f:
			doc = f.read()

		self.feed(doc)

	def handle_starttag(self, tag, attrs):
		self.starttag = tag

	def handle_endtag(self, tag):
		self.endtag = tag

	def handle_data(self, data):
		if self.starttag =='span' or self.starttag == 'td':
			self.data_output.append(float(data))

		elif self.starttag == 'b' and self.endtag != 'b':
			if data not in self.set_ids:
				self.set_ids.append(data)
			else:
				pass

	def dist_table(self):
		n_cols = len(self.set_ids)
		data = np.array(self.data_output).reshape((n_cols,n_cols))

		return pd.DataFrame(data=data, index=self.set_ids, columns=self.set_ids)