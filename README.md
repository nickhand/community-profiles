# community-profiles

A Python toolkit to map data across Philadelphia's communities. The package includes Python software to download and manage datasets about Philadelphia's communities.

## Examples

For example, to download a geopandas GeoDataFrame holding the boundary polygons for the
Public Use Microdata Sample (PUMA) regions in Philadelphia, use:

```python
>>> import community_profiles.datasets as cp_data

>>> pumas = cp_data.PUMAs.get()

>>> pumas
    puma_id                                     puma_name                                           geometry
0   4203201        Philadelphia City (Far Northeast) PUMA  POLYGON ((1763601.383189762 481533.6067272425,...
1   4203203  Philadelphia City (Near Northeast-East) PUMA  POLYGON ((1761015.694895537 477687.8230201704,...
2   4203205                 Philadelphia City (East) PUMA  POLYGON ((1757481.344300119 472641.1848288011,...
3   4203209          Philadelphia City (Center City) PUMA  POLYGON ((1753219.867451427 469259.2878358513,...
4   4203211            Philadelphia City (Southeast) PUMA  POLYGON ((1748035.749563448 465830.1586085176,...
5   4203210            Philadelphia City (Southwest) PUMA  (POLYGON ((1748636.235200001 458712.5695999963...
6   4203207              Philadelphia City (Central) PUMA  POLYGON ((1748959.114121609 475293.3204159532,...
7   4203208                 Philadelphia City (West) PUMA  POLYGON ((1746595.66710492 472893.8219732819, ...
8   4203202  Philadelphia City (Near Northeast-West) PUMA  POLYGON ((1757230.134278996 479915.8414142439,...
9   4203204                Philadelphia City (North) PUMA  POLYGON ((1752340.788933472 478799.6010950198,...
10  4203206            Philadelphia City (Northwest) PUMA  POLYGON ((1745313.497459354 480215.0811579982,...
```

## Development

### Setting up local branches

1. Fork the repository to get a copy under your own user name.

2. Clone the forked repository. From command line:

   ```
   git clone https://github.com/USERNAME/community-profiles.git
   ```

   Now, the "master" branch will be set up to

3. Set up the "upstream" repository so we can keep your forked version up-to-date.

   ```
   git remote add upstream https://github.com/PhiladelphiaController/community-profiles.git
   ```

4. Now, if you run:

   ```
   git remove -v
   ```

   you should see two remote repositories: "origin" and "upstream" listed.

### Workflow steps

1.  Make changes locally and commit them to the "master" branch of your forked repository.
    To add add a file to git control:

        ```
        git add example.py
        ```

        And then you can commit that file with a message:

        ```
        git ci example -m "this is an example commit"
        ```

2.  Next, you can push those changes to your forked repository on Github:

    ```
    git push origin master
    ```

3.  We can merge this new changes back in to the upstream repository ("PhiladelphiaController/community-profiles") using a pull request. Details on
    creating a pull request can be found [here](https://help.github.com/en/articles/creating-a-pull-request).
4.  You can sync changes from the upstream repository by:
    ```
    git pull upstream master --rebase
    ```
    This will sync the master branch of your forked repository with the master branch of the upstream master.
