# Getting started

Depending on your operating system (``<os>``, linux or windows), rename the file ``Pipfile_<os>`` into ``Pipfile``.

```
mkdir .venv
python -m pip install --upgrade setuptools pip
pipenv install -d --python 3.10
```

## Jupyter notebook using pipenv

0. Create a pipenv shell:

```sh
pipenv shell
```

1. Install the pipenv kernelspec for jupyter:

```sh
python -m ipykernel install --user --name=`basename $VIRTUAL_ENV`
```

2. Launch the jupyter notebook:

```sh
jupyter notebook
```

3. From the notebook, select the `.venv` kernel.

# Question answering

## `question_answering_bert_finetuned_squad_demo.ipynb`

**context:**

> Normally the calendar advances 1 day, but you may choose to advance it 2 days instead. This privilege is subject to limitations: You cannot use this privilege if your board is darker side up. When you use this privilege, you must flip your board over to the darker side to show that you have used it. (If you reach the top step of a temple, you can flip it back, as explained in the next section, under 'Temples'.) You may not use this privilege to push off a worker that would not normally be pushed off a gear. In other words, you may not use this privilege if there is a worker on action space 6 of one of the four smallest gears or action space 9 of the Chichen Itza gear. Even if you cannot use the time-speeding privilege, you still get all the other benefits of choosing the Starting Player Space. It is not possible to use this privilege to avoid Food Days. If the next day on the Tzolk'in gear is a Food Day, you may still advance 2 days, but the new round will be the Food Day that was skipped over.

**question:**

> How can a player flip their board back?

**answer:**

> if you reach the top step of a temple

# Resources

## Books

- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
- [Dive into deep learning](https://d2l.ai/index.html)
- [The engineer's guide to deep learning](https://www.interdb.jp/dl/index.html)


## Docs

- [Mistral AI](https://docs.mistral.ai/)
- [DeepSeek](https://api-docs.deepseek.com/)
- [Hugging Face](https://huggingface.co/learn/llm-course/chapter0/1)
- [OpenAI](https://platform.openai.com/docs/overview)
- [Anthropic](https://docs.anthropic.com/en/home)
- [Unsloth](https://docs.unsloth.ai/)

## Academics

- [UvA Deep Learning Tutorials](https://uvadlc-notebooks.readthedocs.io/en/latest/)

## Blogs

- [IBM think](https://www.ibm.com/think/topics)
- [The latest research from Google](https://research.google/blog)
- [Anthropic](https://transformer-circuits.pub/2021/framework/index.html)
- [The AI summer](https://theaisummer.com/positional-embeddings/)
- [Lilian](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/)
- [Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
