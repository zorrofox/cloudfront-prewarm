# CloudFront Prewarm

This python script can help to prewarm static contents which been pushed to edge pop site.

## Prerequirement

1. Python version 3 above.
2. Install required packages:
```bash
pip install -r requirement.txt
```

## Configurations

### url.cfg
All the URLs you want to prewarm. Pelase start a Slash(/) and don't use the domain in this file. Each line will contain a seprate URL and end with a Return(\n) char.

### domain.cfg
The CNAME alias you have setup in China Regions

### edge.cfg
The edge location pop internal code which we have setup all the four China regions: Beijing, Ningxia, Shanghai and Shenzhen. So this file will not need modify.

## Prewarm
When you have set up `url.cfg` and `domain.cfg` you can run:
```bash
python prewarm.py
```
