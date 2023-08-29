# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
# Copyright 2015 and onwards Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nemo_text_processing.inverse_text_normalization.jp.graph_utils import GraphFst
from nemo_text_processing.inverse_text_normalization.jp.verbalizers.cardinal import CardinalFst
from nemo_text_processing.inverse_text_normalization.jp.verbalizers.decimal import DecimalFst
from nemo_text_processing.inverse_text_normalization.jp.verbalizers.fraction import FractionFst
from nemo_text_processing.inverse_text_normalization.jp.verbalizers.ordinal import OrdinalFst
from nemo_text_processing.inverse_text_normalization.jp.verbalizers.whitelist import WhiteListFst


class VerbalizeFst(GraphFst):
    """
    Composes other verbalizer grammars.
    For deployment, this grammar will be compiled and exported to OpenFst Finite State Archive (FAR) File.
    More details to deployment at NeMo/tools/text_processing_deployment.
    """

    def __init__(self):
        super().__init__(name="verbalize", kind="verbalize")
        cardinal = CardinalFst()
        cardinal_graph = cardinal.fst

        ordinal = OrdinalFst()
        ordinal_graph = ordinal.fst

        decimal = DecimalFst()
        decimal_graph = decimal.fst

        fraction = FractionFst()
        fraction_graph = fraction.fst

        whitelist_graph = WhiteListFst().fst
        graph = cardinal_graph | ordinal_graph | decimal_graph | fraction_graph | whitelist_graph
        self.fst = graph