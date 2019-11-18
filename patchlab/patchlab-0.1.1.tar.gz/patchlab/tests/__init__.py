# flake8: noqa
import os

from django.db.models.signals import post_save
from django.test import TestCase
import vcr


TEST_ROOT = os.path.dirname(os.path.realpath(__file__))
FIXTURES = os.path.join(TEST_ROOT, "fixtures")


class BaseTestCase(TestCase):
    """Base class for Django tests."""

    def setUp(self):
        """Common setup for tests."""
        # Import here because the Django app isn't set up until here.
        from patchwork.models import Patch

        post_save.disconnect(sender=Patch, dispatch_uid="patchlab_mr")
        my_vcr = vcr.VCR(
            cassette_library_dir=os.path.join(FIXTURES, "VCR/"), record_mode="once"
        )
        self.vcr = my_vcr.use_cassette(self.id())
        self.vcr.__enter__()
        self.addCleanup(self.vcr.__exit__, None, None, None)


SINGLE_COMMIT_MR = """Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [TEST PATCH] Bring balance to the equals signs
From: Patchwork <patchwork@patchwork.example.com>
To: kernel@lists.fedoraproject.org
Cc: Administrator <admin@example.com>
Reply-To: kernel@lists.fedoraproject.org
Date: Mon, 04 Nov 2019 23:00:00 -0000
Message-ID: <4@localhost.localdomain>
X-Patchlab-Patch-Author: Jeremy Cline <jcline@redhat.com>
X-Patchlab-Merge-Request: https://gitlab/root/kernel/merge_requests/1
X-Patchlab-Commit: a958a0dff5e3c433eb99bc5f18cbcfad77433b0d

This is a silly change so I can write a test.

Signed-off-by: Jeremy Cline <jcline@redhat.com>
---
 README | 1 +
 1 file changed, 1 insertion(+)

diff --git a/README b/README
index 669ac7c32292..a0cc9c082916 100644
--- a/README
+++ b/README
@@ -1,3 +1,4 @@
+============
 Linux kernel
 ============
 
-- 
2.22.0

"""

MULTI_COMMIT_MR = [
    """Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [TEST PATCH 0/2] Update the README
From: Patchwork <patchwork@patchwork.example.com>
To: kernel@lists.fedoraproject.org
Cc: Administrator <admin@example.com>
Reply-To: kernel@lists.fedoraproject.org
Date: Mon, 04 Nov 2019 23:00:00 -0000
Message-ID: <1@localhost.localdomain>
X-Patchlab-Merge-Request: https://gitlab/root/kernel/merge_requests/2

Update the README to make me want to read it more.""",
    """Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [TEST PATCH 1/2] Bring balance to the equals signs
From: Patchwork <patchwork@patchwork.example.com>
To: kernel@lists.fedoraproject.org
Cc: Administrator <admin@example.com>
Reply-To: kernel@lists.fedoraproject.org
Date: Mon, 04 Nov 2019 23:00:00 -0000
Message-ID: <2@localhost.localdomain>
X-Patchlab-Patch-Author: Jeremy Cline <jcline@redhat.com>
X-Patchlab-Merge-Request: https://gitlab/root/kernel/merge_requests/2
X-Patchlab-Commit: 5c9b066a8bc9eed0e8d7ccd392bc8f77c42532f0

This is a silly change so I can write a test.

Signed-off-by: Jeremy Cline <jcline@redhat.com>
---
 README | 1 +
 1 file changed, 1 insertion(+)

diff --git a/README b/README
index 669ac7c32292..a0cc9c082916 100644
--- a/README
+++ b/README
@@ -1,3 +1,4 @@
+============
 Linux kernel
 ============
 
-- 
2.22.0

""",
    """Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [TEST PATCH 2/2] Convert the README to restructured text
From: Patchwork <patchwork@patchwork.example.com>
To: kernel@lists.fedoraproject.org
Cc: Administrator <admin@example.com>
Reply-To: kernel@lists.fedoraproject.org
Date: Mon, 04 Nov 2019 23:00:00 -0000
Message-ID: <4@localhost.localdomain>
X-Patchlab-Patch-Author: Jeremy Cline <jcline@redhat.com>
X-Patchlab-Merge-Request: https://gitlab/root/kernel/merge_requests/2
X-Patchlab-Commit: c321c86ee75491f4bc0b0b0e368f71eff88fa91c

Make the README more readable.

Signed-off-by: Jeremy Cline <jcline@redhat.com>
---
 README => README.rst | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename README => README.rst (100%)

diff --git a/README b/README.rst
similarity index 100%
rename from README
rename to README.rst
-- 
2.22.0

""",
]

SINGLE_PATCH_GIT_AM_FAILURE = """
Hello,

We were unable to apply this patch series to the current development branch.
The current head of the master branch is commit abc123.

Please rebase this series against the current development branch and resend it
or, if you prefer never seeing this email again, submit your series as a pull
request:

  1. Create an account and fork https://gitlab.example.com/root/kernel.
  2. git remote add <remote-name> <your-forked-repo>
  3. git push <remote-name> <branch-name> --push-option=merge_request.create \\
       --push-option=merge_request.title="[TEST] Bring balance to the equals signs"
"""

MULTI_PATCH_GIT_AM_FAILURE = """
Hello,

We were unable to apply this patch series to the current development branch.
The current head of the master branch is commit abc123.

Please rebase this series against the current development branch and resend it
or, if you prefer never seeing this email again, submit your series as a pull
request:

  1. Create an account and fork https://gitlab.example.com/root/kernel.
  2. git remote add <remote-name> <your-forked-repo>
  3. git push <remote-name> <branch-name> --push-option=merge_request.create \\
       --push-option=merge_request.title="Update the README"
"""

BIG_EMAIL = """Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [TEST PATCH 0/2] Update the README
From: Patchwork <patchwork@patchwork.example.com>
To: kernel@lists.fedoraproject.org
Cc: Administrator <admin@example.com>
Reply-To: kernel@lists.fedoraproject.org
Date: Mon, 04 Nov 2019 23:00:00 -0000
Message-ID: <4@localhost.localdomain>
X-Patchlab-Merge-Request: https://gitlab/root/kernel/merge_requests/2

Update the README to make me want to read it more.

Note:

The patch series is too large to sent by email.

Reviewing locally, set up your repository to fetch from the GitLab remote:

  $ git remote add gitlab https://gitlab/root/kernel.git
  $ git config remote.gitlab.fetch '+refs/merge-requests/*:refs/remotes/origin/merge-requests/*'
  $ git fetch gitlab

Finally, check out the merge request:

  $ git checkout merge-requests/2

It is also possible to review the merge request on GitLab at:
    https://gitlab/root/kernel/merge_requests/2
"""
