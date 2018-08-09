# -*-coding:utf-8-*-
# Author: alphadl
# ensemble_translate.py 2018/8/3 21:26

# !/usr/bin/env python
from __future__ import division, unicode_literals
import argparse
from onmt.translate.translator import build_translator
from onmt.utils import logging
# import onmt.io
# import onmt.translate
# import onmt
# import onmt.model_builder
# import onmt.modules
import onmt.opts


def main(opt):
    translator = build_translator(opt, report_score=True, logger=logger,
                                  use_ensemble=True)
    # translator.translate(opt.src_dir, opt.src, opt.tgt,
    #                      opt.batch_size, opt.attn_debug)
    translator.translate(src_path=opt.src,
                         tgt_path=opt.tgt,
                         src_dir=opt.src_dir,
                         batch_size=opt.batch_size,
                         attn_debug=opt.attn_debug)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='ensemble_translate.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    onmt.opts.add_md_help_argument(parser)
    onmt.opts.translate_opts(parser, use_ensemble=True)

    opt = parser.parse_args()
    logger = logging.init_logger(opt.log_file)
    main(opt)

if __name__ == '__main__':
    print ""
